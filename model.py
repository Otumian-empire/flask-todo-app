from datetime import datetime
import sqlite3


class Model:

    def __init__(self):
        """ connect to the database and create a cursor """
        try:
            self.DATABASE = 'to_do_app'
            self.conn = sqlite3.connect(self.DATABASE)
            self.cur = self.conn.cursor()

        except Exception as e:
            if self.cur:
                self.cur.close()
            print(e)

    def close(self):
        """ commit changes, close the cursor and connection """
        self.conn.commit()
        self.cur.close()
        self.conn.close()


class Task(Model):

    # task : id, name, date

    def __init__(self):
        """ create table if table does not exist """
        try:
            self.model = Model()
            self.model.cur.execute(
                """CREATE TABLE IF NOT EXISTS `task` (
                    `id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	                `name`	TEXT NOT NULL,
	                `date`	TEXT NOT NULL
                );""")

        except Exception as e:
            print(e)
        finally:
            self.model.close()

    def insert_task(self, name):
        """ insert task by name and date

        date is the current date
        """
        try:
            date = datetime.now().strftime('%d-%B-%Y')
            sql = "INSERT INTO `task`(`name`, `date`) values(?, ?)"

            return self.model.cur.execute(sql, name, date).rowcount

        except Exception as e:
            print(e)
        finally:
            self.model.close()

    def read_task(self, id=''):
        """ read task using id """
        try:
            sql = "SELECT * FROM `task`"

            if not id:
                id = ''
                return self.model.cur.execute(sql).fetchall()
            else:
                sql += " where id = ?"
                return self.model.cur.execute(sql, id).fetchone()

        except Exception as e:
            print(e)
        finally:
            self.model.close()

    def update_task(self, new_name, id):
        """ update task name using id """
        try:
            sql = "UPDATE FROM `task` SET `name` = ? WHERE `id` = ?"

            return self.model.cur.execute(sql, new_name, id).rowcount

        except Exception as e:
            print(e)
        finally:
            self.model.close()

    def delete_task(self, id):
        """ delete task using id """
        try:
            sql = "DELETE FROM `task` WHERE `id` = ?"

            return self.model.cur.execute(sql, id).rowcount

        except Exception as e:
            print(e)
        finally:
            self.model.close()


class Time:

    # time : id, task_id, time

    def __init__(self):
        """ create table if table does not exist """
        try:
            self.model = Model()
            self.model.cur.execute(
                """CREATE TABLE IF NOT EXISTS `time` (
                	`id`	INTEGER NOT NULL,
                    `task_id`	INTEGER NOT NULL,
                    `time`	TEXT NOT NULL,
                    PRIMARY KEY(`id`)
                );""")

        except Exception as e:
            print(e)
        finally:
            self.model.close()

    def insert_time(self, task_id, time):
        """ insert time for task using task_id,  passing the time """
        try:
            sql = "INSERT INTO `time` (`task_id`, `time`) VALUES(?, ?);"
            return self.model.cur.execute(sql, task_id, time).rowcount

        except Exception as e:
            print(e)
        finally:
            self.model.close()

    def read_time(self, task_id=''):
        """ read time for task using task_id """
        try:
            sql = "SELECT * FROM `time"
            if not task_id:
                return self.model.cur.execute(sql).fetchall()
            else:
                sql += " WHERE `task_id` = ?"
                return self.model.cur.execute(sql, task_id).fetchone()

        except Exception as e:
            print(e)
        finally:
            self.model.close()

    def update_time(self, task_id, time):
        """ update time for task using task_id, passing the time"""
        try:
            sql = "UPDATE `time` SET `time` = ? WHERE `task_id` = ?"

            return self.model.cur.execute(sql, time, task_id).rowcount

        except Exception as e:
            print(e)
        finally:
            self.model.close()

    def delete_time(self, task_id):
        """ delete time for task using task_id """
        try:
            sql = "DELETE FROM `time` WHERE `task_id` = ?"

            return self.model.cur.execute(sql, task_id).rowcount

        except Exception as e:
            print(e)
        finally:
            self.model.close()

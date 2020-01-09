from datetime import datetime
import sqlite3


class model:

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

    def run_query(self):
        raise NotImplementedError

    def close(self):
        """ commit changes, close the cursor and connection """
        self.conn.commit()
        self.cur.close()
        self.conn.close()


class Task(model):

    # task : id, name, date

    def __init__(self):
        """ create table if table does not exist """
        try:
            self.model = model()
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
            return self.model.cur.execute(sql, name, date).rowcount()

        except Exception as e:
            print(e)
        finally:
            self.model.close()

    def read_task(self, id):
        """ read task using id """
        try:
            sql = "SELECT * FROM task"

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
            sql = "UPDATE FROM `task` SET `name` = ? WHERE id = ?"

            return self.model.cur.execute(sql, new_name, id).rowcount()

        except Exception as e:
            print(e)
        finally:
            self.model.close()

    def delete_task(self, id):
        """ delete task using id """
        try:
            sql = "DELET FROM `task` WHERE id = ?"

            return self.model.cur.execute(sql, id).rowcount()

        except Exception as e:
            print(e)
        finally:
            self.model.close()


class Time:

    # time : id, task_id, start, end

    def __init__(self):
        """ create table if table does not exist """
        try:
            self.TABLE = 'time'
            model = model()
            model.cur.execute(
                """CREATE TABLE IF NOT EXISTS `task` (`id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,`name` TEXT NOT NULL,`date` TEXT NOT NULL)""")

        except Exception as e:
            print(e)
        finally:
            model.conn.commit()

    def insert_time(self, task_id, start, end):
        """ insert time for task using task_id, passing the start and end """
        model.conn.commit()

    def read_time(self, task_id):
        """ read time for task using task_id """
        pass

    def update_time(self, task_id, start, end):
        """ update time for task using task_id, passing the start and end """
        pass

    def delete_time(self, task_id):
        """ delete time for task using task_id """
        pass

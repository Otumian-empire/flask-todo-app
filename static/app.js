jQuery(function () {

    // all constants
    // maximum and minimum number of characters required
    const MAX_TEXT_COUNT = 30
    const MIN_TEXT_COUNT = 3
    let class_name = 'danger'


    // all ajax calls
    // insert
    // make ajax request to send data to the database
    $('#addBtn').on('click', function (e) {
        e.preventDefault()

        $.ajax({
            url: `/add`,
            type: 'POST',
            dataType: 'json',
            data: {
                item: $('#input').val()
            },
            success: function (response) {
                $('#input').val('')
                location.reload(true)
            }
        })
    })

    // read
    $.ajax({
        url: `/read`,
        type: `POST`,
        dataType: 'json',
        success: function (response) {
            status = response['status']
            payload = response['payload']

            if (status) {
                for (i = 0; i < payload.length; i++) {
                    add_item(payload[i].id, payload[i].item)
                }
                $('#table').prepend()
            } else {
                console.log(playl)
            }

        }
    })

    // update

    // delete

    // all event triggered functionalities
    // count the input that user enters
    $('#input').on('keyup', function () {

        remove_paragraph(class_name)

        class_name = 'danger'

        $('#counter').text($('#input').val().length)

        // reduce the input to MAX_TEXT_COUNT when user 
        // enters more text than MAX_TEXT_COUNT
        if ($('#input').val().length > MAX_TEXT_COUNT) {

            $('#input').val($('#input').val().substring(0, MAX_TEXT_COUNT))
            $('#counter').text($('#input').val().length)

            call_alert('Maximum text count exceeded ' + MAX_TEXT_COUNT, class_name);

        } else {
            remove_paragraph(class_name)
        }

    })

    // add item to the list
    $('#add').on('click', function (e) {
        e.preventDeault()

        // remove class if there is any
        remove_paragraph(class_name)

        class_name = 'warning'

        // check minimum length
        if ($('#input').val().length < MIN_TEXT_COUNT) {
            call_alert('Minimum text count not reached ' + MIN_TEXT_COUNT, class_name)
        } else {
            remove_paragraph(class_name);
            // suppress add_item() name and do a console log
            // console.log()
            // add_item()
            call_alert('Item added successfully', 'success')
        }
    })


    // all named functions
    /**
     * remove a paragraph
     */
    function remove_paragraph(class_name) {
        $('p').removeClass(class_name)
        $('p').remove()
    }

    /**
     * call alert
     */
    function call_alert(message, class_name) {
        var p = $("<p id='alert' class='" + class_name + "'></p>")
        p.text(message)
        $('.group').after(p)

    }

    /**
     * add an item to the list
     */
    function add_item(id, task) {
        var td_id = $("<td></td>")
        td_id.text(id)

        var td_task = $("<td></td>")
        td_task.text(task)

        var td_btn = $("<td></td>")

        var btn = $('<button></button>')
        btn.attr('id', id)
        btn.text('close')
        btn.addClass('close-btn')

        td_btn.append(btn)

        var tr = $("<tr></tr>")
        tr.append(td_id)
        tr.append(td_task)
        tr.append(td_btn)

        $('#table').prepend(tr)

        $('#input').val('')
        $('#counter').text($('#input').val().length)

        $('.close-btn').on('click', function () {
            // make request to remove item from the database
            $.ajax({
                url: `/delete/${id}`,
                type: 'DELETE',
                dataType: 'json',
                success: function (response) {

                    if (response.response_object['status'] === 1) {
                        $(`#${id}`).parent().parent().remove()
                        location.reload(true)
                    }

                    $('#firstName').val('')
                    $('#lastName').val('')

                }
            })
        })

    }

})
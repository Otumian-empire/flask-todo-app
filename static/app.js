jQuery(function () {

    // maximum and minimum number of characters required
    var maxTextCount = 30
    var minTextCount = 3

    // count the input that user enters
    $('#input').on('keyup', function () {

        remove_paragraph(class_name)

        var class_name = 'danger'

        $('#counter').text($('#input').val().length)

        // reduce the input to maxTextCount when user 
        // enters more text than maxTextCount
        if ($('#input').val().length > maxTextCount) {

            $('#input').val($('#input').val().substring(0, maxTextCount))
            $('#counter').text($('#input').val().length)

            call_alert('Maximum text count exceeded ' + maxTextCount, class_name);

        } else {
            remove_paragraph(class_name)
        }

    })

    // add item to the list
    // $('#add').on('click dblclick', function (e) {
    //     e.preventDeault()

    //     // remove class if there is any
    //     remove_paragraph(class_name)
    //     var class_name = 'warning'

    //     // check minimum length
    //     if ($('#input').val().length < minTextCount) {
    //         call_alert('Minimum text count not reached ' + minTextCount, class_name)
    //     } else {

    //         remove_paragraph(class_name);
    //         add_item()
    //         call_alert('Item added successfully', 'success')

    //     }
    // })

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
    function add_item() {

        var span = $('<span></span>')
        span.text($('#input').val())

        // make ajax request to send data to the database

        var btn = $('<button></button>')
        btn.text('close')
        btn.addClass('close-btn')

        var clr = $('<div></div>')
        clr.addClass('clr')

        var li = $('<li></li>')
        li.append(span)
        li.append(btn)
        li.append(clr)

        $('#list').prepend(li)

        $('#input').val('')
        $('#counter').text($('#input').val().length)


        $('.close-btn').on('click', function () {

            console.log('removed it')
            // make request to remove item from the database
            $(this).parent().remove()

        })
    }

})

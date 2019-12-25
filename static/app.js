jQuery(function () {

    var maxTextCount = 30
    var minTextCount = 3

    $('#input').on('keyup', function () {

        remove_paragraph(class_name)

        var class_name = 'danger'

        $('#counter').text($('#input').val().length)

        if ($('#input').val().length > maxTextCount) {

            $('#input').val($('#input').val().substring(0, maxTextCount))
            $('#counter').text($('#input').val().length)

            call_alert('Maximum text count exceeded ' + maxTextCount, class_name);

        } else {
            remove_paragraph(class_name)
        }

    })

    $('#add').on('click dblclick', function () {
        remove_paragraph(class_name)
        var class_name = 'warning'

        if ($('#input').val().length < minTextCount) {
            call_alert('Minimum text count not reached ' + minTextCount, class_name)
        } else {

            remove_paragraph(class_name);
            add_item()
            call_alert('Item added successfully', 'success')

        }
    })

    function remove_paragraph(class_name) {

        $('p').removeClass(class_name)
        $('p').remove()

    }

    function call_alert(message, class_name) {

        var p = $("<p id='alert' class='" + class_name + "'></p>")
        p.text(message)
        $('.group').after(p)

    }

    function add_item() {

        var span = $('<span></span>')
        span.text($('#input').val())

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
            $(this).parent().remove()

        })
    }

})

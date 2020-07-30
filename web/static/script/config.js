$('.update').click(function () {
    name = $(this).attr('inputname');
    value = $(document.getElementsByName(name)).val();
    if (name == 'masscan') {
        value = value + "|" + $('#rate').val()
    }
    alert(value)
    $.post('/config', {
        'name': name,
        'value': value,
        'contype': location.toString().split('?')[1].split('=')[1]
    }, function (data) {
        if (data == 'success') {
            swal("更新成功", "", "success")
        } else {
            swal("更新失败", "请检查数据完整性", "error")
        }
    })
});
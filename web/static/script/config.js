$('.update').click(function () {
    name = $(this).attr('inputname');
    value = $(document.getElementsByName(name)).val();
    if (name == 'masscan') {
        value = value + "|" + $('#rate').val()
    }
    $.post('/config', {
        'name': name,
        'value': value,
        'conftype': location.toString().split('?')[1].split('=')[1]
    }, function (data) {
        if (data == 'success') {
            swal("更新成功", "", "success")
        } else {
            swal("更新失败", "请检查数据完整性", "error")
        }
    })
});
$('#masscan_flag').change(function () {
    name = 'masscan_flag';
    conftype = 'assetscan';
    value = $(this).is(":checked") == true ? 1 : 0;
    $.post('/config', {
        'name': name,
        'conftype': conftype,
        'value': value,
    }, function (data) {
        if (data == 'patherror') {
            $('#masscan_flag').click()
            swal("切换失败", '未检测到masscan，请先安装或先配置正确的路径', 'error');
        } else if (data == 'fail') {
            swal('切换失败', '请检查数据完整性', 'error')
        }
    });
});
$('#icmp_flag').change(function () {
    name = 'port_list_flag'
    value = $(this).is(':checked') == true ? 1 : 0
    conftype = 'assetscan'
    $.post('/config', {
        'name': name,
        'conftype': conftype,
        'value': value
    }, function (data) {
        if (data == 'fail') {
            swal('切换失败', '请检查数据完整性', 'error')
        }
    })
});
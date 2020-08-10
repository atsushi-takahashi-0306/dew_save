$(function () {


     function red_list(url,list) {
        $(window).bind('load', function () {
            if(document.URL.match(url)) {
                $(list).css('color', 'red');
            }
        });
    }
    red_list('all_wine/','.nav_list1');
    red_list('detail_wine/','.nav_list1');
    red_list('my_wine/','.nav_list2');
    red_list('update_wine/','.nav_list2');
    red_list('add_wine/','.nav_list3');
    red_list('update_user/','.nav_list4');

});



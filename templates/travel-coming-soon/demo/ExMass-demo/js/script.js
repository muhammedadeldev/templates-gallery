(function ($) {
  "use strict";
  Pace.on("start", function () {
    $("#preloader").show();
  });
  Pace.on("done", function () {
    $('#status').fadeOut(); // will first fade out the loading animation
    $('#preloader').delay(1000).fadeOut('slow'); // will fade out the white DIV that covers the website.
    setTimeout(checkForm, 1000);



    var wow = new WOW(
            {
              boxClass: 'wow', // animated element css class (default is wow)
              animateClass: 'animated', // animation css class (default is animated)
              offset: '-200px', // distance to the element when triggering the animation (default is 0)
              mobile: true, // trigger animations on mobile devices (default is true)
              live: true        // act on asynchronously loaded content (default is true)
            }
    );

    new WOW().init();

    var winWidth = $(window).outerWidth();
    var winHeight = $(window).outerHeight();
// set initial div height / width
    $('.wrapper').css({
      width: winWidth,
      height: winHeight
    });
// make sure div stays full width/height on resize
    $(window).resize(function () {
      var winWidth = $(window).outerWidth();
      var winHeight = $(window).outerHeight();

      $('.wrapper').animate({
        'width': winWidth,
        'height': winHeight
      }, 0);
    });



if($('#countdown_dashboard').length>0){
    $('#countdown_dashboard').countDown({
      targetDate: {
        'day': 1,
        'month': 1,
        'year': 2023,
        'hour': 0,
        'min': 0,
        'sec': 0
      }
    });
    }

//    Style1
    if ($('body.style1').length > 0) {

      $('#bg-glow').plaxify({"xRange": 20, "yRange": 20});
      $('#glows-up').plaxify({"xRange": 80, "yRange": -40});
      $('#glows-down').plaxify({"xRange": -50, "yRange": 60});
      $.plax.enable();

      hitTheLights();
      $(window).resize(function () {
        hitTheLights();
      });

    }


    function hitTheLights() {
      var winWidth = $(window).outerWidth();
      var winHeight = $(window).outerHeight();


      var newWnH = Math.min(winWidth, winHeight);
      $('#lights1,#lights2,#lights3').css({'width': newWnH + 'px'}).css({'height': newWnH + 'px'});
      $('.page-holder').css({'width': newWnH - 50 + 'px'});



    }



//    Style2
    if ($('body.style2').length > 0) {

      $('#bg-glow').plaxify({"xRange": 20, "yRange": 20});
      $('#glows-up').plaxify({"xRange": 80, "yRange": -40});
      $('#lights1').plaxify({"xRange": 50});
      $('#lights2').plaxify({"xRange": -50});
      $.plax.enable();


      $(window).resize(function () {

      });

    }



    function getImgSize(el, imgSrc) {
      var newImg = new Image();
      newImg.onload = function () {
        var height = newImg.height;
        var width = newImg.width;

        el.css('height', height);

      };
      newImg.src = imgSrc;
    }

    if ($('.bg-image[data-bg-image]').length > 0) {
      $('.bg-image[data-bg-image]').each(function () {
        var el = $(this);
        var sz = getImgSize(el, el.attr("data-bg-image"));
        el.css('background-position', 'center').css('background-image', "url('" + el.attr("data-bg-image") + "')").css('background-size', 'cover').css('background-repeat', 'no-repeat');
      });
    }



    $('[data-placeholder]').focus(function () {
      var input = $(this);
      if (input.val() === input.attr('data-placeholder')) {
        input.val('');

      }
    }).blur(function () {
      var input = $(this);
      if (input.val() === '' || input.val() === input.attr('data-placeholder')) {
        input.addClass('placeholder');
        input.val(input.attr('data-placeholder'));
      }
    }).blur();

    $('[data-placeholder]').parents('form').submit(function () {
      $(this).find('[data-placeholder]').each(function () {
        var input = $(this);
        if (input.val() === input.attr('data-placeholder')) {
          input.val('');
        }
      });
    });



    function checkForm() {
      if ($(".form-holder").length > 0) {

        var formStatus = $(".form-holder form").validate();

        //   ===================================================== 
        //sending contact form
        $(".form-holder form").submit(function (e) {
          e.preventDefault();

          //  triggers contact form validation

          if (formStatus.errorList.length === 0)
          {
            $(".form-holder form").fadeOut(function () {
              $('#loading').css('visibility', 'visible');
              $.post('submit.php', $(".form-holder form").serialize(),
                      function (data) {

                        $('.message-box').html(data);


                        $('#loading').css('visibility', 'hidden');

                      }

              );
            });


          }

        });
      }
    }



  });






})(jQuery);


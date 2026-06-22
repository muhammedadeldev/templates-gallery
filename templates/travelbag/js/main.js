
  $(document).ready(function(){

  // preloader - start

  $(window).on('load', function () {
    $('#preloader').fadeOut('slow', function () { $(this).remove(); });
  });
  setTimeout(function()
  { $('#preloader').addClass('d-none'); }, 3000);
  
  // preloader - end

  $(document).on("scroll", function(){
    if
      ($(document).scrollTop() > 86){
      $("#banner").addClass("shrink");
    }
    else
    {
      $("#banner").removeClass("shrink");
    }
  });  


  $(function() {
        $(document).scroll(function() {
            var $nav = $("#mainNavbar");
            $nav.toggleClass("scrolled", $(this).scrollTop() > $nav.height());
        });
    });



  //smooth scroll
    $('.nav-link').on('click', function (e) {
        var anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $(anchor.attr('href')).offset().top
        }, 1000);
        e.preventDefault();
    });

  //top header


 // for video-version
    $(".player").mb_YTPlayer();


   // youtube video js start here
    jQuery("a.bla-1").YouTubePopUp({
        autoplay: 0
    });

  // gallery

   $(".gallery-details .gallery-img").click(function () {
        var $src = $(this).attr("src");
        $(".show").fadeIn();
        $(".img-show img").attr("src", $src);
    });
    
    $("span, .overlay").click(function () {
        $(".show").fadeOut();
    });

//scroll buttton


if ($(window).scrollTop() < 100) {
    $('.scrollToTop').hide();
  }
  
  $(window).scroll(function() {
    if ($(this).scrollTop() > 100) {
      $('.scrollToTop').fadeIn('slow');
    } else {
      $('.scrollToTop').fadeOut('slow');
    }
  });
  $('.scrollToTop').click(function(){
    $('html, body').stop().animate({scrollTop:0}, 500, 'swing');
    return false;
  });
  
//header

  var headerId = $(".sticky-header");
  var headerTop = $(".sticky-header .header-top");

  $(window).on('scroll', function () {
    var amountScrolled = $(window).scrollTop();
    if ($(this).scrollTop() > 50) {
      headerId.removeClass("not-stuck");
      headerId.addClass("stuck");
      headerTop.addClass("display-none");
    } else {
      headerId.removeClass("stuck");
      headerId.addClass("not-stuck");
      headerTop.removeClass("display-none");
    }
  });

  //destination

  $('.owl-carousel').owlCarousel({
    loop:true,
    slideToshow:3,
    slideToscroll:3,
    speed:30,
    margin:10,
    nav:true,
    autoplay:true,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:3
        },
        1000:{
            items:4
        }
    }
  })

  //testimonials 


  /*Clients Review*/
    $("#client-slider").owlCarousel({
        items:1,
        itemsDesktop:[1000,2],
        itemsDesktopSmall:[990,1],
        itemsTablet:[768,1],
        pagination:false,
        navigation:true,
        navigationText:["",""],
        slideSpeed:1000,
        autoPlay:false
    });


    $('#contact_form .from-button').click(function () {
    $.ajax({
        type: 'post',
        url: 'mail.php',
        data: $('#contact_form').serialize(),
        success: function () {
          $('#contact_form')[0].reset();
          $('#contact_form .from-button').attr('style', "background-color:#16C39A");
          $('#contact_form .from-button').siblings().html("<i style='color:#16C39A'>*</i> Email has been sent successfully");
        }
    });
    return false;
    });

    
});




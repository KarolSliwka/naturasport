$(document).ready(function () {
  /**
   * This function will display scroll-up button
   */
  $(window).scroll(function () {
    if ($(this).scrollTop() > 100) {
      $(".scroll-top").fadeIn();
    } else {
      $(".scroll-top").fadeOut();
    }
  });

  $(".scroll-top").click(function () {
    $("html, body").animate(
      {
        scrollTop: 0,
      },
      100
    );
    return false;
  });

  /**
   * Toggle hamburger button
   */
  $(document).ready(function () {
    $(".hamburger").click(function () {
      $(this).toggleClass("is-active");
    });
  });

  /**
   * This function will display toasts
   */
  $(".toast").toast("show");
});

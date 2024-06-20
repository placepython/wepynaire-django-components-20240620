document.addEventListener("alpine:init", () => {
  Alpine.data("slider", () => ({
    swiper: null,

    init() {
      this.swiper = new Swiper(this.$el, {
        // Optional parameters
        loop: true,

        // If we need pagination
        pagination: {
          el: ".swiper-pagination",
        },

        // Navigation arrows
        navigation: {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev",
        },

        // And if we need scrollbar
        scrollbar: {
          el: ".swiper-scrollbar",
        },
      });
    },
  }));
});

function navbar() {
    return {
        open: false,

        toggle() {
            this.open = !this.open;
        }
    };
}
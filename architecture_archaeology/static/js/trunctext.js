'use strict';
window.addEventListener('load', () => {
    let intro = new ShowMore('description', 'read_more', 300);
});
function ShowMore(e, l, stop) {
    this.e = document.getElementById(e);
    this.stop = stop;
    this.l = document.getElementById(l);
    // 1. Keep a reference of your original string
    this.originalTxt = this.e.innerText;

    this.l.addEventListener('click', (e) => {
      this.expand_text();
      e.preventDefault();
      e.stopPropagation();
    });

    this.get_length = () => {
        return this.e.innerText.length;
    };

    this.hide_text = () => {
      this.e.innerText = this.e.innerText.substr(0, this.stop) + '\u2026';
      this.l.style.display = 'inline';
      this.e.appendChild(this.l);
    }
    // 2. revert to original text, stored in local variable
    this.expand_text = () => {
      this.e.innerText = this.originalTxt;
    }

    this.show = () => {
    return (this.get_length() > this.stop) ? this.hide_text() : this.expand_text();
    };

    this.show();
};
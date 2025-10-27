// ? TRIGGERING TASKBAR ELEMENTS
const fsToggle = document.querySelector("#fullscreen-toggle");
import { BrowserDefaults } from "../base/base.js";

// & EVENT LISTENER FOR FULLSCREEN TOGGLE
fsToggle.addEventListener('click', () => {
    if (document.body.classList.contains('fs')) {
        document.exitFullscreen();
        fsToggle.querySelector('.icon').src = "/static/assets/icons/common/fullscreen.png"
        document.body.classList.remove('fs');
        BrowserDefaults.enable();
    } else {
        document.documentElement.requestFullscreen().catch(console.log);
        fsToggle.querySelector('.icon').src = "/static/assets/icons/common/regular.png"
        document.body.classList.add('fs');
        BrowserDefaults.disable();
    }
})
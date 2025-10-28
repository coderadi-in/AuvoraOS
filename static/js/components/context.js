// ? IMPORTING LIBRARIES
import { closePopup, openPopup } from '../base/base.js';

// ? SETTING UP SOME VALUES
const contextMenu = document.querySelector("#main-context-menu");
const refreshBtn = document.querySelector("#refresh");
const settingsBtn = document.querySelector("#settings");
const newFolderBtn = document.querySelector("#folder");
const newTextBtn = document.querySelector("#text");
const displaySettingsBtn = document.querySelector("#display-settings");
const accountBtn = document.querySelector("#account");

// ? POPUP WINDOWS
const newFolderPopup = document.querySelector("#new-folder-popup");

// & EVENT LISTENER FOR [REFRESH] BUTTONS
refreshBtn.addEventListener("click", () => {
    location.reload();
});

// & EVENT LISTENER FOR [NEW FOLDER] BUTTON
newFolderBtn.addEventListener("click", () => {
    openPopup(newFolderPopup);
});

// & EVENT LISTENER FOR CONTEXT MENU
document.addEventListener("contextmenu", (e) => {
    e.preventDefault();

    const menuWidth = contextMenu.offsetWidth;
    const menuHeight = contextMenu.offsetHeight;
    const pageWidth = window.innerWidth;
    const pageHeight = window.innerHeight;

    // Default position
    let posX = e.pageX;
    let posY = e.pageY;

    // Adjust if the menu would overflow the right or bottom edge
    if (posX + menuWidth > pageWidth) {
        posX = pageWidth - menuWidth - 10; // small margin
    }
    if (posY + menuHeight > pageHeight) {
        posY = pageHeight - menuHeight - 10;
    }

    // Show and position menu
    openPopup(contextMenu);
    contextMenu.classList.add('open');
    contextMenu.style.top = `${posY}px`;
    contextMenu.style.left = `${posX}px`;
});

// & EVENT LISTENER TO CLOSE CONTEXT MENU
document.addEventListener("click", (e) => {
    if (contextMenu.classList.contains('open')) {
        contextMenu.classList.remove('open');
        closePopup(contextMenu);
    }
});

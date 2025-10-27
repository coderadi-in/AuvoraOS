// ? Importing modules
import { closePopup, openPopup } from "../base/base.js";
import { vfs } from '../base/vfs.js';

// ? SETTING UP some values
const days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
const months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'];
const newFolderBtn = document.querySelector('#new-folder');
const closeNewFolderBtn = document.querySelector("#close-new-folder");
const newFolderPopup = document.querySelector("#new-folder-popup");

// * FUNCTION to update time
function updateTime() {
    const now = new Date();
    const hours = now.getHours().toString().padStart(2, '0');
    const minutes = now.getMinutes().toString().padStart(2, '0');
    const seconds = now.getSeconds().toString().padStart(2, '0');
    const formattedTime = `${hours}:${minutes}:${seconds}`;
    document.querySelector('#current-time').innerHTML = formattedTime;

    if (formattedTime == '00:00:00') {updateDate();}
}

// * FUNCTION to update date
function updateDate() {
    const now = new Date();
    const day = days[now.getDay()];
    const date = now.getDate();
    const month = months[now.getMonth()];
    const year = now.getFullYear();
    const formattedDate = `${day}, ${month} ${date} &bull; ${year}`
    document.querySelector("#current-date").innerHTML = formattedDate;
}

// | FUNCTION CALL for date & time update
updateTime();
updateDate();

setInterval(() => {
        updateTime();
}, 1000);

// & EVENT LISTENER for new-folder button click
newFolderBtn.addEventListener('click', () => {
    openPopup(newFolderPopup);
});

// & EVENT LISTENER for close-new-folder button click
closeNewFolderBtn.addEventListener('click', () => {
    closePopup(newFolderPopup);
})
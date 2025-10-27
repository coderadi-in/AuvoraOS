// * FUNCTIONALITY to disable/enable certain browser default behaviors
export const BrowserDefaults = (() => {
  const prevent = e => e.preventDefault();
  const events = ['contextmenu', 'selectstart', 'dragstart', 'auxclick'];

  function enable() {
    events.forEach(evt => document.removeEventListener(evt, prevent));
    window.removeEventListener('keydown', blockKeys);
    console.log('✅ Browser defaults restored.');
  }

  function disable() {
    events.forEach(evt => document.addEventListener(evt, prevent));
    window.addEventListener('keydown', blockKeys);
    console.log('🚫 Browser defaults disabled.');
  }

  function blockKeys(e) {
    const key = e.key.toLowerCase();
    const blocked =
      e.key === 'F1' ||
      e.key === 'F3' ||
      e.key === 'F5' ||
      e.key === 'F7' ||
      e.key === 'F11' ||
      e.key === 'F12' ||
      e.ctrlKey ||
      e.altKey;

    if (blocked) e.preventDefault();
  }

  return { enable, disable };
})();

// * FUNCTION to open popups
export const openPopup = ((popup) => {
  popup.style.display = "flex";

  setTimeout(() => {
    popup.style.opacity = "1";
  }, 100);
})

// * FUNCTION to close popups
export const closePopup = ((popup) => {
  popup.style.opacity = "0";

  setTimeout(() => {
    popup.style.display = "none";
  }, 300);
})
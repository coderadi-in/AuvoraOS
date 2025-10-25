// * FUNCTIONALITY to disable/enable certain browser default behaviors
const BrowserDefaults = (() => {
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
      e.key === 'F5' ||
      e.key === 'F12' ||
      (e.ctrlKey && ['r', 'u', 's', 'p'].includes(key)) ||
      (e.ctrlKey && e.shiftKey && ['i', 'j', 'c'].includes(key));

    if (blocked) e.preventDefault();
  }

  return { enable, disable };
})();

export default BrowserDefaults;
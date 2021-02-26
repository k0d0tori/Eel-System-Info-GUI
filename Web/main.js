function vrl() {
  function display(cpu_perc, memr, disc) {
    document.getElementById('cpu_perc').innerHTML = cpu_perc;
    document.getElementById('memr').innerHTML = memr;
    document.getElementById('disc').innerHTML = disc;
  }
  eel.expose(display);
}

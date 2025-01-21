//DOM is Document Object Model
<div id="container">
  <div class="display">hey</div>
  <div class="controls">yo</div>
</div>                                        
// selects the .controls div
const controls = document.querySelector(".controls");

// selects the prior sibling => .display
const display = controls.previousElementSibling;
console.log(display); // <div class="display"></div>    
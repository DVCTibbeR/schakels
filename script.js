let btn = document.createElement("button");

btn.style.margin = "10px";
btn.innerHTML = "Switch light on";

document.body.appendChild(btn);

let lightOn = false

btn.addEventListener("click", (_ev) => {
	btn.textContent = lightOn ? "Switch light off" : "Switch light on";
	document.body.style.backgroundColor = lightOn ? "black" : "yellow";

	console.log(lightOn ? "light is off" : "light is on");

	lightOn = !lightOn;
});
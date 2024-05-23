function gera_input(item, parent){
	var row = document.createElement('div')
	row.className = 'row mt-1'
	
	var col = document.createElement('div')
	col.className = 'col'
	
	var label = document.createElement('label')
	label.innerHTML = item.label_innerHTML
	
	var input = document.createElement('input')
	input.type = item.type
	input.name = item.name	
	input.className = 'form-control'
	input.classList.add(item.input_class)
	
	col.appendChild(label)
	col.appendChild(input)
	row.appendChild(col)
	$(parent).append(row)
}

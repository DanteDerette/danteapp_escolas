function gera_input(item, parent){
	
	var para_inputs_arr = [
		'text',
		'number',
		'date'
	]

	var para_inputs_arr_file = [
		'file'
	]

	var para_select_arr = ['select']

	if(para_inputs_arr.includes(item.type)){
		para_inputs(item, parent)
	} else if(para_select_arr.includes(item.type)){
		para_select(item, parent)
	} else if(para_inputs_arr_file.includes(item.type)){
		para_inputs_file(item, parent)
	}

}

function para_inputs_file(item, parent){
	var row = document.createElement('div')
	row.className = 'row mt-1'
	
	var col = document.createElement('div')
	col.className = 'col'
	
	var label = document.createElement('label')
	if(item.required){
		item.label_innerHTML += `
			<span style='color: red'>*</span>
		`
	}
	label.innerHTML = item.label_innerHTML
	
	var input = document.createElement('input')
	input.type = item.type
	input.name = item.name	
	input.accept = "image/*"
	if(item.disabled){
		input.disabled = item.disabled
	}
	if(item.required){
		input.required = item.required
	}

	if(item.func_oninput){
		input.oninput = (e) => {
			item.func_oninput(e.currentTarget)
		}
	}

	input.className = 'form-control'
	input.autocomplete = 'one-time-code'
	input.classList.add(item.input_class)
	
	col.appendChild(label)
	col.appendChild(input)
	row.appendChild(col)
	$(parent).append(row)

}

function para_select(item, parent){
	var row = document.createElement('div')
	row.className = 'row mt-1'
	
	var col = document.createElement('div')
	col.className = 'col'
	
	var label = document.createElement('label')
	label.innerHTML = item.label_innerHTML
	
	var select = document.createElement('select')
	select.name = item.name	
	select.className = 'form-select'
	select.classList.add(item.input_class)
	col.appendChild(label)
	col.appendChild(select)

	item.opts_arr.forEach((
		opt, index
	) => {
		var option = document.createElement('option')
		option.innerHTML = item.opt_arr_innerHTML[index]
		option.value = opt
		select.appendChild(option)
	})

	
	row.appendChild(col)
	$(parent).append(row)
}

function tira_is_invalid(elemento){
	elemento.classList.remove('is-invalid')
}

function para_inputs(item, parent){
	var row = document.createElement('div')
	row.className = 'row mt-1'
	
	var col = document.createElement('div')
	col.className = 'col'
	
	var label = document.createElement('label')
	if(item.required){
		item.label_innerHTML += `
			<span style='color: red'>*</span>
		`
	}
	label.innerHTML = item.label_innerHTML
	
	var input = document.createElement('input')
	input.type = item.type
	input.name = item.name	
	if(item.disabled){
		input.disabled = item.disabled
	}
	if(item.required){
		input.required = item.required
	}

	if(item.func_oninput){
		input.oninput = (e) => {
			item.func_oninput(e.currentTarget)
		}
	}

	input.className = 'form-control'
	input.autocomplete = 'one-time-code'
	input.classList.add(item.input_class)
	
	col.appendChild(label)
	col.appendChild(input)
	row.appendChild(col)
	$(parent).append(row)
}

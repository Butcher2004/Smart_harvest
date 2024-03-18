

function updateInput()
{    
    var selectedCrop = document.getElementById("cropSelect").value;

    console.log(selectedCrop);
}

function moveToNext(event, nextFieldId) {
    if (event.key === 'Enter') { 
        // event.preventDefault(); 
        document.getElementById(nextFieldId).focus(); 
    }
}
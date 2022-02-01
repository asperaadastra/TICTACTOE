let resultField = document.getElementById('cl1');

let cells = Array.from(document.getElementsByClassName('cell'));

cells.map(cell =>{
    cell.addEventListener('click', (prop)=>{
      switch(prop.target.innerText){
          case 'o':
          resultField.innerText= 'x';
      }
}
}
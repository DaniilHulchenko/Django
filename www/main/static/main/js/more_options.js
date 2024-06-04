document.querySelector('#more_options_wrapper').onmouseover = ()=>{document.querySelector('#more_options').showModal();};
document.querySelector('#more_options_wrapper').onmouseout = () =>{ document.querySelector('#more_options').close();};
document.querySelector('#nav-btn').onmouseover = ()=>{document.querySelector('#more_options').showModal();};



// document.querySelector('#more_options').onmouseover = () =>{ document.querySelector('#more_options').showModal();};

// document.querySelector('#more_options').onclick = (e)=>{
// 			if (e.target != document.querySelector('#more_options')){
// 				document.querySelector('#more_options').close();
// 				// document.querySelector('#more_options').showModal();
// 			}
// 			else{
// 				// document.querySelector('#more_options').close();
// 			}
// 				console.log(e.target)
// 	};

// document.querySelector('#more_options').onclick= (e)=>{ console.log(e.target);};
// document.querySelector('#more_options').onmouseout = ()=>{document.querySelector('#more_options').close();};
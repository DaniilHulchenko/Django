// sign in open
    const openModalSI = document.querySelector('.openModalSI');
    const ModalSI = document.querySelector('#sign_in');
    // openModalSI.addEventListener('click', () => {
    //     ModalSI.showModal();
    // });
    openModalSI.onclick = ()=>{
        ModalSI.showModal();
    };
    // close
    const closeModalSI = document.querySelector('.closeModalSI');
    closeModalSI.onclick = function(e){
        if (e.target == document.querySelector(".closeModalSI")){
            ModalSI.close();
        }
    }
    // closeModalSI.addEventListener( 'click', (e) => {
    //     if (e.target == document.querySelector(".closeModalSI")){
    //         ModalSI.close();
    //     }
    // });
// sing up open
    const openModalSU = document.querySelector(".openModalSU");
    const ModalSU = document.querySelector("#sign_up");

    openModalSU.addEventListener('click', ()=> {
        ModalSU.showModal();
    })
    // close 
    const closeModalSU = document.querySelector('.closeModalSU');
    closeModalSU.addEventListener( 'click', (e) => {
        if (e.target == document.querySelector(".closeModalSU")){
            ModalSU.close();
        }
    });

//    const already_have_account = document.querySelector(".already_have_account")
//    already_have_account.onclick = function()=>{
//        document.querySelector("#sign_up").close();
//        document.querySelector("#sign_in").showModal();
//    };

    //   Already have account
    document.querySelector(".already_have_account").onclick = ()=>{
        ModalSU.close();
        ModalSI.showModal();
    };





// closeModalSISI.addEventListener( 'click', () => {
//     if (closeModalSISI != document.querySelector('#signin'))
//     document.querySelector('#sign_in').close ( )
// }

// function closeModalSISI(e){
//     if(e.target == document.querySelector('#signin')) document.querySelector('#signin').close()
//     console.log(e.target)
// }
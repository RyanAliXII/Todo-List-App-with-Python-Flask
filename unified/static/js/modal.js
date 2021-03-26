const createBtn = document.querySelector('.create-action')
const formwrapper = document.querySelector('.form-wrapper')

createBtn.addEventListener('click',()=>{
    formwrapper.className = "form-wrapper"
})
const closeModal = ()=>{
    formwrapper.className = "form-wrapper hide"
    console.log("HELLO")
}
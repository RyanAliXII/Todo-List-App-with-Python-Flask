const BASE_URL = 'http://localhost:5000'

let todo = { }
const loader = document.querySelector('.loader');

const showLoader = ()=>{
    loader.className = "loader"
}
const hideLoader = ()=>{
    loader.className = "loader hide"
}
const fetchTodos = async()=>{
    showLoader();
    const populateList = (lists) => {
        const ul = document.querySelector("#todo-lists")
        ul.innerHTML = " "; // clear list before appending
        lists.forEach(todo=>{
            const list = document.createElement('li');
            const divDetails = document.createElement('div');
            divDetails.className = "todo-details"
            const divActions = document.createElement('div')
            divActions.className = "todo-actions"
            const spanTitle = document.createElement('span')
            spanTitle.className = "todo-title"
            spanTitle.innerText = todo.title
            const spanBody = document.createElement('span')
            spanBody.className = "todo-body"
            spanBody.innerText = todo.body;
            const spanStatus = document.createElement('span')
            spanStatus.className = "todo-status"
            spanStatus.innerText = todo.isDone ? "Done" : "Undone"
            
            divDetails.append(spanTitle)
            divDetails.append(spanBody)
            divDetails.append(spanStatus)
            const deleteAction = document.createElement('i')
            deleteAction.className = "fas fa-trash"
            deleteAction.addEventListener('click',() =>{
              const id = todo.id; 
              deleteTodo(id);
            })
            const markAction = document.createElement('i')
            markAction.addEventListener('click',() =>{
                const id = todo.id; 
                markAsDone(id);
              })
            markAction.className = "fas fa-check"
            divActions.append(markAction)
            divActions.append(deleteAction)
            list.append(divDetails)
            list.append(divActions)
            list.className = "todo-list"
        
            ul.append(list)
        })
    }
    try{
        const {data} = await axios.get(`${BASE_URL}/todos`);
        populateList(data.todos)
    }
    catch(error){
        console.log(error)
    }
    finally{
        hideLoader()
    }
 
}
fetchTodos();

const createTodo = async() =>{
    try{
        const {data:response} = await axios.post(`${BASE_URL}/todos/`,todo);
        if(response.message === "OK"){
            fetchTodos();
        }

    }catch(error){
        console.log(error)
    }
   
}
const deleteTodo = async(id)=>{
    try{
        const {data:response} = await axios.delete(`${BASE_URL}/todos/${id}`)
        if(response.message === "OK"){
            fetchTodos();
        }
    }
    catch(error){
        console.log(error)
    }
   

}
const markAsDone = async(id)=>{
    try{
        const {data:response} = await axios.patch(`${BASE_URL}/todos/${id}`)
        if(response.message === "OK"){
            fetchTodos();
        }
    }catch(error){
        console.log(error)
    }
}

const handleInputs = (input) => {
    todo = Object.assign(todo, {[input.name]:input.value});
}

const handleSubmit = (event) => {
    createTodo();
 
    
}


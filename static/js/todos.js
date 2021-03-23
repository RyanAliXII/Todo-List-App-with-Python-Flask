const BASE_URL = 'http://localhost:5000'

let todo = { }

const fetchTodos = async()=>{
    try{
        const {data} = await axios.get(`${BASE_URL}/todos`);
        console.log(data);
    }
    catch(error){
        console.log(error)
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
const deleteTodo = async()=>{

}
const markAsDone = async()=>{
    
}

const handleInputs = (input) => {
    todo = Object.assign(todo, {[input.name]:input.value});
}
const handleSubmit = (event) => {
    createTodo();
 
    
}
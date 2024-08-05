import axios from "axios"

async function getMoodBoard() {
  return await axios.get("http://localhost:8080/api/elements")
}

async function addText(content) {
  return await axios.post("http://localhost:8080/api/elements", {
    type: "text",
    content
  })
}

async function addImage() {
  return await axios.post("http://localhost:8080/api/elements", {
    type: "Image",
    content: "https://source.unsplash.com/300x300"
  })
}

async function deleteElement(id) {
  return await axios.delete(`http://localhost:8080/api/element/${id}`)
}

export { getMoodBoard, addText, addImage, deleteElement }
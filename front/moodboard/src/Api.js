import axios from "axios"

async function getMoodBoard() {
  return await axios.get("http://localhost:8080/elements")
}

async function addText(content) {
  return await axios.post("http://localhost:8080/elements/create", {
    type: "text",
    content
  })
}

async function addImage() {
  return await axios.post("http://localhost:8080/elements/create", {
    type: "Image",
    content: "https://source.unsplash.com/300x300"
  })
}

export { getMoodBoard, addText, addImage }
import React, { useEffect } from "react";
import { useState } from "react";

import "./index.css";
import MoodBoard from "./MoodBoard.js";
import { addText, addImage, getMoodBoard } from "./Api"

const Buttons = (props) => {
  useEffect(() => {
    handleLoad(props);
  }, []);

  const handleLoad = async (props) => {
    const moodBoardElements = (await getMoodBoard()).data
    
    moodBoardElements && moodBoardElements.forEach(element => {
      console.log(element.type, element.content)
      if (element.type === "text") {
        props.setTexts(prevState => [...prevState, element.content])
      }
      if (element.type === "Image") {
        props.setImages(prevState => [...prevState, element.content])
      }
    })
  }

  const handleClickText = async (props) => {
    try {
      const response = await addText(props.textField)

      const { content } = response.data

      props.setTexts(prevState => [...prevState, content])
    } catch (error) {
      console.log(`Error: ${error}`)
    }
  }

  const handleClickImage = async (props) => {
    try {
      const response = await addImage()

      const { content } = response.data

      props.setImages(prevState => [...prevState, content])
    } catch (error) {
      console.log(`Error: ${error}`)
    }
  }

  return (
    <ul>
      <button onClick={() => handleClickText(props)}>Add Text</button>
      <button onClick={() => handleClickImage(props)}>Add Image</button>
    </ul>
  )
}

function App() {
  const [textField, setTextField] = useState("");
  const [images, setImages] = useState([""]);
  const [texts, setTexts] = useState([""]);

  return (
    <div className="container ">
      <div className="navbar">
        <div className="header font-title">MoodBoard</div>
        <input type="text" placeholder="Text" onChange={e => setTextField(e.target.value)}/>
        <Buttons 
          textField={textField}
          images={images}
          texts={texts}
          setImages={setImages}
          setTexts={setTexts}
          />
        <div className="footer ont-secondary" />
      </div>

      <MoodBoard
        images={images}
        texts={texts}
      />
    </div>
  );
}
export default App;
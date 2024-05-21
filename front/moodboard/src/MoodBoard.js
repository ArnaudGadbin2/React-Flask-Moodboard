import React from "react"
import { Stage, Layer, Image, Text } from "react-konva"

class URLImage extends React.Component {
  state = {
    image: null
  }

  componentDidMount() {
    this.loadImage()
  }

  componentDidUpdate(oldProps) {
    if (oldProps.src !== this.props.src) {
      this.loadImage()
    }
  }

  componentWillUnmount() {
    this.image.removeEventListener("load", this.handleLoad)
  }

  loadImage() {
    this.image = new window.Image()
    this.image.src = this.props.src
    this.image.addEventListener("load", this.handleLoad)
  }

  handleLoad = () => {
    this.setState({
      image: this.image
    })
  }

  handleDragEnd = e => {
    this.setState({
      x: e.target.x,
      y: e.target.y
    })
  }

  render() {
    return (
      <Image
        image={this.state.image}
        ref={node => {
          this.imageNode = node;
        }}
        x={window.innerWidth / 2}
        y={window.innerHeight / 2}
        shadowColor="black"
        shadowBlur={10}
        shadowOpacity={0.6}
        draggable
        onDragEnd={this.handleDragEnd}
        onDragStart={() => {
          this.setState({
            isDragging: true
          })
        }}
      />
    )
  }
}

class TextElem extends React.Component {

  state = {
    text: this.props.src
  }

  handleDragEnd = e => {
    this.setState({
      x: e.target.x,
      y: e.target.y
    })
  }

  render() {
    return (
      <Text
        text={this.state.text}
        ref={node => {
          this.imageNode = node;
        }}
        x={window.innerWidth / 2}
        y={window.innerHeight / 2}
        shadowColor="black"
        shadowBlur={10}
        shadowOpacity={0.6}
        draggable
        onDragEnd={this.handleDragEnd}
        onDragStart={() => {
          this.setState({
            isDragging: true
          })
        }}
      />
    )
  }
}

function MoodBoard(props) {
  return (
    <Stage width={window.innerWidth} height={window.innerHeight}>
      <Layer>
        {
          props.images.map((image , i)=> (
            <URLImage src={image} key={i}/>
          ))
        }
        {
          props.texts.map((text, i) => (
            <TextElem src={text} key={i}/>
          ))
        }
      </Layer>
    </Stage>
  );
}

export default MoodBoard;

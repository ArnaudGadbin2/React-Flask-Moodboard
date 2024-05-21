import React from "react";

function ListItem(props) {
  return (
    <li>
      <div className="avatar" />
      <div>
        <div className="title font-title">Title</div>
        <div className="date font-secondary">
          <span className="date">11/11/2019</span>{" "}
          <span className="description">Description</span>
        </div>
      </div>
    </li>
  );
}

export default ListItem;

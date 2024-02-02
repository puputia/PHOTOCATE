import React, { Component } from "react";
// import styled from "styled-components";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faFolder } from "@fortawesome/free-solid-svg-icons";
import { Button, Row, Col } from "react-bootstrap";
import "../App.css";

export class ShareFolder extends Component {
  render() {
    return (
      <Row
        className="mx-auto"
        style={{ textAlign: "center", alignItems: "center" }}
      >
        {/* button */}
        <Col style={{ margin: "10px", maxWidth: "15rem" }}>
          <Button
            variant="outline-success"
            style={{
              border: "solid 1px #cccccc",
              backgroundColor: "white",
              color: "black",
            }}
          >
            <FontAwesomeIcon
              icon={faFolder}
              style={{ height: "20vh", color: "#A286DB" }}
            />
            <div>먹을거</div>
          </Button>
        </Col>

        <Col style={{ margin: "10px", maxWidth: "15rem" }}>
          <Button
            style={{
              border: "solid 1px #cccccc",
              backgroundColor: "white",
              color: "black",
            }}
          >
            <FontAwesomeIcon
              icon={faFolder}
              style={{ height: "20vh", color: "#A286DB" }}
            />
            <div>먹을거</div>
          </Button>
        </Col>

        <Col style={{ margin: "10px", maxWidth: "15rem" }}>
          <Button
            style={{
              border: "solid 1px #cccccc",
              backgroundColor: "white",
              color: "black",
            }}
          >
            <FontAwesomeIcon
              icon={faFolder}
              style={{ height: "20vh", color: "#A286DB" }}
            />
            <div>먹을거</div>
          </Button>
        </Col>

        <Col style={{ margin: "10px", maxWidth: "15rem" }}>
          <Button
            style={{
              border: "solid 1px #cccccc",
              backgroundColor: "white",
              color: "black",
            }}
          >
            <FontAwesomeIcon
              icon={faFolder}
              style={{ height: "20vh", color: "#A286DB" }}
            />
            <div>먹을거</div>
          </Button>
        </Col>
      </Row>
    );
  }
}

export default ShareFolder;

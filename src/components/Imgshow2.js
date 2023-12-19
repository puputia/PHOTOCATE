// Imgshow2.js

import React from 'react';
import { Container, Row, Col, Card } from 'react-bootstrap';

const Imgshow2 = ({ images }) => {
  return (
    <Container>
      <Row style={{ textAlign: "center", alignItems: "center" }}>
        {images.map((image, index) => (
          <Col key={index} style={{ margin: "10px" }}>
            <Card style={{ maxWidth: "15rem" }}>
              <Card.Img
                variant="top"
                src={image.src}
                alt={`Card image ${index}`}
                style={{ height: "28vh" }}
              />
              <Card.Body>
                <Card.Title>{image.title}</Card.Title>
                {/* 추가적인 정보가 있다면 아래 주석을 풀고 사용하세요. */}
                {/* <Card.Text>{image.description}</Card.Text> */}
              </Card.Body>
            </Card>
          </Col>
        ))}
      </Row>
    </Container>
  );
};

export default Imgshow2;
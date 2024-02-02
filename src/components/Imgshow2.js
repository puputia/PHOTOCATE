import React from 'react';
import { Container, Row, Col, Card } from 'react-bootstrap';
import { useNavigate } from 'react-router-dom'; // Import useNavigate hook

const Imgshow2 = ({ images }) => {
  const navigate = useNavigate(); // Initialize useNavigate

  const handleImageClick = () => {
    // Handle image click and navigate to Edit.js
    navigate('/PhotoEdit');
  };

  return (
    <Container>
      <Row style={{ textAlign: 'center', alignItems: 'center' }}>
        {images.map((image, index) => (
          <Col key={index} style={{ margin: '10px' }} onClick={handleImageClick}>
            {/* Make the Card component clickable */}
            <Card style={{ maxWidth: '15rem', cursor: 'pointer' }}>
              <Card.Img
                variant="top"
                src={image.src}
                alt={`Card image ${index}`}
                style={{ height: '28vh' }}
              />
              <Card.Body>
                <Card.Title>{image.title}</Card.Title>
              </Card.Body>
            </Card>
          </Col>
        ))}
      </Row>
    </Container>
  );
};

export default Imgshow2;

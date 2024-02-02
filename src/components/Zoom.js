import React from "react";
import { TransformWrapper, TransformComponent, useControls } from "react-zoom-pan-pinch";
import { Button } from "react-bootstrap";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faSearchPlus, faSearchMinus, faRedo } from "@fortawesome/free-solid-svg-icons";

const Controls = () => {
  const { zoomIn, zoomOut, resetTransform } = useControls(); // useControls를 어떻게 가져오는지에 따라 수정 필요

  return (
    <>
      <Button onClick={() => zoomIn()}>
        <FontAwesomeIcon icon={faSearchPlus} /> Zoom In
      </Button>
      <Button onClick={() => zoomOut()}>
        <FontAwesomeIcon icon={faSearchMinus} /> Zoom Out
      </Button>
      <Button onClick={() => resetTransform()}>
        <FontAwesomeIcon icon={faRedo} /> Reset
      </Button>
    </>
  );
};

const Zoom = () => {
  return (
    <TransformWrapper>
      {({ zoomIn, zoomOut, resetTransform }) => (
        <div>
          {/* 이미지에 적용할 Controls */}
          <Controls />

          {/* 추가적인 컨텐츠 */}
          <div>
            {/* 다른 컨텐츠 */}
          </div>

          {/* 이미지를 감싸는 TransformComponent */}
          <TransformComponent>
            <img src="test.jpg" alt="test" />
          </TransformComponent>
        </div>
      )}
    </TransformWrapper>
  );
};

export default Zoom;
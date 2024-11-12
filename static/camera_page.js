let videoStream = null;
const videoElement = document.getElementById("video");
const canvasElement = document.getElementById("canvas");
const capturedImageElement = document.getElementById("capturedImage");
const errorElement = document.getElementById("error");
const analyzeButton = document.getElementById("analyzeButton");

async function startCamera() {
    try {
        videoStream = await navigator.mediaDevices.getUserMedia({ video: true });
        videoElement.srcObject = videoStream;
        errorElement.textContent = "";
    } catch (err) {
        console.error("Error accessing the camera", err);
        errorElement.textContent = "카메라에 접근할 수 없습니다. 브라우저 설정을 확인해주세요.";
    }
}

function captureImage() {
    const context = canvasElement.getContext("2d");
    canvasElement.width = videoElement.videoWidth;
    canvasElement.height = videoElement.videoHeight;

    if (context && videoElement) {
        context.drawImage(videoElement, 0, 0, canvasElement.width, canvasElement.height);
        const imageDataUrl = canvasElement.toDataURL("image/jpeg");
        capturedImageElement.src = imageDataUrl;
        capturedImageElement.classList.remove("hidden");
        analyzeButton.disabled = false;
    }
}
// async function analyzeImage() {
//     analyzeButton.textContent = "처리 중...";
//     analyzeButton.disabled = true;
//
//     // 실제 모델 분석을 요청하는 대신 대기 시간 시뮬레이션
//     await new Promise((resolve) => setTimeout(resolve, 2000));
//
//     analyzeButton.textContent = "확인하기";
//     analyzeButton.disabled = false;
//     alert("이미지 분석 완료!");
//
//     // 캡처된 이미지 데이터를 세션 스토리지에 저장
//     const imageData = capturedImageElement.src;
//     sessionStorage.setItem('capturedImage', imageData);
//
//     // '결과 페이지'로 리디렉션
//     window.location.href = `../결과 페이지/result.html`;
// }
async function analyzeImage() {
    analyzeButton.textContent = "처리 중...";
    analyzeButton.disabled = true;

    // 실제 모델 분석을 요청하는 대신 대기 시간 시뮬레이션
    await new Promise((resolve) => setTimeout(resolve, 2000));

    analyzeButton.textContent = "확인하기";
    analyzeButton.disabled = false;
    alert("이미지 분석 완료!");

    // 캡처된 이미지 데이터를 세션 스토리지에 저장
    const imageData = capturedImageElement.src;
    sessionStorage.setItem('capturedImage', imageData);

    // '결과 페이지'로 리디렉션 (Django URL 구조에 맞게 수정)
    window.location.href = '/result_page/';  // 결과 페이지 URL로 변경
}
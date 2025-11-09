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
//     // '결과 페이지'로 리디렉션 (Django URL 구조에 맞게 수정)
//     window.location.href = '/result_page/';  // 결과 페이지 URL로 변경
// }
async function analyzeImage() {
    analyzeButton.textContent = "처리 중...";
    analyzeButton.disabled = true;

    const imageData = capturedImageElement.src; // Base64 이미지 데이터

    try {
        // Django 백엔드로 이미지 전송
        const response = await fetch('/analyze/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCsrfToken(), // CSRF 토큰 추가
            },
            body: JSON.stringify({ image: imageData }),
        });

        if (response.ok) {
            const result = await response.json(); // 분석 결과 받기
            const { pill_code } = result;

            // 결과 페이지로 리디렉션, pill_code 전달
            window.location.href = `/result_page/?pill_code=${pill_code}`;
        } else {
            alert("이미지 분석 실패. 다시 시도해주세요.");
        }
    } catch (err) {
        console.error("Error analyzing image:", err);
        alert("서버와 통신하는 중 오류가 발생했습니다.");
    } finally {
        analyzeButton.textContent = "확인하기";
        analyzeButton.disabled = false;
    }
}

// CSRF 토큰 가져오기 함수
function getCsrfToken() {
    const cookies = document.cookie.split(';');
    for (const cookie of cookies) {
        if (cookie.trim().startsWith('csrftoken=')) {
            return cookie.trim().substring('csrftoken='.length);
        }
    }
    return '';
}
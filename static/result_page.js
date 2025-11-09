let isSaving = false;

function goBack() {
    alert("다시 촬영 페이지로 이동합니다.");
    // Django URL 구조에 맞게 페이지 이동 경로 수정
    window.location.href = "/camera_page/";  // Django URL로 리디렉션
}

function saveResult() {
    const saveButton = document.getElementById("saveButton");
    if (isSaving) return;

    isSaving = true;
    saveButton.textContent = "저장 중...";
    saveButton.disabled = true;

    // 서버에 데이터를 저장하는 실제 로직으로 교체
    setTimeout(() => {
        alert("결과가 저장되었습니다.");
        isSaving = false;
        saveButton.textContent = "사용 이력 저장";
        saveButton.disabled = false;
        window.location.href = "/main_page/";  // 저장 후 메인 페이지로 리디렉션
    }, 1000);
}

window.onload = function() {
    const imageData = sessionStorage.getItem('capturedImage');
    if (imageData) {
        const resultImage = document.getElementById('resultImage');
        if (resultImage) {
            resultImage.src = imageData;
        }
    }
};

현재 참여 인원 ( 10명 )
도흔 승훈 현진 부광 동엽 지훈 은찬 은송 희원 은우

#######################################################################################

1. anaconda prompt 실행, 새로운 환경 만들기 -> conda create -n style python=3.7

2. 새로운 환경 실행 -> conda activate style

3. pytorch 설치(cuda가 없는 것 같은 경우 꼭!!!! 말해주기!!!!!) -> conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch

4. 터미널에서 압축 푼 파일로 이동 -> cd [파일경로]/STYLETRANSFER

5. 다음을 실행하여 style_transfer 설치 -> pip install -e ./style-transfer-pytorch-master

6. 동봉된 auto를 열어서 파일 경로를 지정해준다.
   - 필요한 폴더:
      /val2014 :: ms coco 사이트에서 다운받기
      /style :: 압축파일에 포함
      /style_2014 :: output 폴더, 본인이 직접 만들기
   - 코드에서 수정이 필요한 부분:
   base_folder :: 이미지 폴더들이 있는 경로 -> 본인이 설정해주기

7. auto.py 실행 -> python auto.py [본인이름]
   ex) python auto.py 이승훈

#######################################################################################
c=1;
Y=imread('breast_Xray.tif');
doubleY=double(Y);
negativeY=255-Y;
subplot(1,2,1);
negativeY1=uint8(negativeY);
imshow(negativeY1);
subplot(1,2,2);
imshow(Y);
figure;
moon=imread('moon.tif ');
subplot(1,2,1);
imshow(moon);

for i=1:540
 for j=1:466
  if moon(i,j)>60
   moon(i,j)=255;
  else
   moon(i,j)=0;
  end
 end
end
figure;
imshow(moon);

load('barbara_dft_no_log.mat');
s=255*c.*log10(1+(barbara_dft_no_log./255));
s1=uint8(s);
figure;
imshow(s1);

x=imread('washed_aerial.tif');
imshow(x);
 for t=3:5
    for i=1:769,
      for j=1:765
        spower(i,j)=255*c*(x(i,j)/255)^t;
      end
    end
    imshow(uint8(spower));
 end
 c=1;
fractured=imread('fractured_spine.tif');
figure;
imshow(fractured);
re=double(fractured);
g=[0.3 0.4 0.6];
for e=1:3
for i=1:976
for j=1:746
s2power(i,j)=255*c*(re(i,j)/255)^g(e);

end
end
figure;
imshow(uint8(s2power));
end
iris=imread('fractal_iris.tif');
iris1=double(iris);
A=255.*bitget(iris1,7);
imshow(uint8(A));
B=255.*bitget(iris1,6);
figure;
imshow(uint8(B));
C=255.*bitget(iris1,6);
figure;
imshow(uint8(C));
D=255.*bitget(iris1,1);
figure;
imshow(uint8(D));
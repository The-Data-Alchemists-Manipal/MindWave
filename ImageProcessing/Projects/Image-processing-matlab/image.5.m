image=imread('circuit-board-pepper.tif');
figure;
imshow(image);
filteredIm=ordfilt2(image,9,ones(3,3));
figure;
imshow(filteredIm);
%%%
image2=imread('circuit-board-salt.tif');
figure;
imshow(image2);
filteredIm2=ordfilt2(image2,1,ones(5,5));
figure;
imshow(filteredIm2);

%%%

IM1=imread('pattern_noise1.tif');
figure;
imshow(IM1);
IM2=imread('pattern_noise2.tif');
figure;
imshow(IM2);
IM3=imread('pattern_noise3.tif');
figure;
imshow(IM3);
figure;
imhist(IM1); %% Rayleigh
figure;
imhist(IM2); %% erlang
figure;
imhist(IM3); %% gaussian noise

%%

ORIimage=imread('pattern.tif');
figure;
imshow(ORIimage);
figure;

imhist(ORIimage);
figure
imshow(imnoise(ORIimage,'salt & pepper'));
figure;
imhist(imnoise(ORIimage,'salt & pepper'));

%%

ORIimage=imread('pattern.tif');
figure;
imshow(ORIimage);
figure;
imhist(ORIimage);
imnoise(ORIimage,'gaussian',0,0.01);
figure;
imshow(imnoise(ORIimage,'gaussian',0,0.01));
figure;
imhist(imnoise(ORIimage,'gaussian',0,0.01));
img=imread('skeleton_orig.tif');
padimg=padarray(img,[1,1],'symmetric','both');
figure;
imshow(img);
imgdouble=double(padimg);
%laplacian
simpleLaplacianfilter=[0 1 0;1 -4 1;0 1 0];
convimg=conv2(padimg,simpleLaplacianfilter,'same');
figure;
imshow(convimg,[]);
%sharpining
sharping=[0 -1 0;0 5 0;0 -1 0];
convimg2=conv2(padimg,sharping,'same');
figure
imshow(uint8(convimg2));
%sobel
sobelrow=[-1 -2 -1;0 0 0;1 2 1];
sobelcolumn=[-1 0 1;-2 0 2;-1 0 1];
convimg3=conv2(padimg,sobelrow,'same');
conving4=conv2(padimg,sobelcolumn,'same');
sobel1=abs(convimg3);
sobel2=abs(conving4);
sobelTOT=sobel1+sobel2;
figure;
imshow(uint8(sobelTOT));
%avaraging
avarageM=ones(5)./5^2;
avaragesobel=conv2(sobelTOT,avarageM,'same');
figure;
imshow(uint8(avaragesobel));
%product/mask
mask=convimg2.*avaragesobel;
figure;
imshow(mask,[]);
%sum a and e
sumsharpened=imgdouble+avaragesobel;
figure;

imshow(sumsharpened,[]);
c=1;
gama=0.98;
maxs=max(max((sumsharpened)));
s=((sumsharpened./5.781600000000001e+02).^gama)*5.781600000000001e+02;
figure;
imshow(uint8(s),[]);
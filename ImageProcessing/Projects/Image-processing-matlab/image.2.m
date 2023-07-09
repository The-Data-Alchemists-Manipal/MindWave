a=imread('checker.tif');
D = padarray(a,[11 11],0,'both');
imshow(D);
avarageM=ones(23)./23^2;
doubleD=double(D);
Csame = conv2(D,avarageM,'same');
Csame1=uint8(Csame);
figure;
imshow(Csame1);
figure;
imshow(uint8(Csame(12:523,12:523)));

F = padarray(a,[11 11],255,'both');
new=conv2(F,avarageM,'same');
figure;
imshow(F);
figure;
imshow(uint8(new));
figure;
imshow(uint8(new(12:523,12:523)));

G= padarray(a,[11 11],'symmetric','both');
new2=conv2(G,avarageM,'same');
figure;
imshow(G);
figure;
imshow(uint8(new2));
figure;
imshow(uint8(new2(12:523,12:523)));


b=imread('hubble_orig.tif');
figure;
imshow(b);
b1=double(b);
avarageM2=ones(15)./(15^2);
imm2= conv2(b1,avarageM2,'same');

figure;
imshow(uint8(imm2));

for i=1:528
    for j=1:485
        if imm2(i,j)>=60;
            imm2(i,j)=255;
        else
            imm2(i,j)=0;
        end
    end
end
figure;
imshow(uint8(imm2));
avarageM3=ones(31)./(31^2);
imm3= conv2(b1,avarageM3,'same');
figure;
imshow(uint8(imm3));

for i=1:528
    for j=1:485
        if imm3(i,j)>=60;
            imm3(i,j)=255;
        else
            imm3(i,j)=0;
        end
    end
end
figure;
imshow(uint8(imm3));

Q=imread('board.tif');
figure;
imshow(Q);
Q1=double(Q);
figure;
imshow(uint8(medfilt2(Q1,[3 3])));

avarageM4=ones(3)./(3^2);
CONVQ1=conv2(Q1,avarageM3,'same');
figure;
imshow(uint8(CONVQ1));
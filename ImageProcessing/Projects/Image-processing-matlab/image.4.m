circuitimg=imread('circuit.tif');
subplot(2,3,1);
imshow('circuit.tif');
doubleCircuit=double(circuitimg);
avarageM=ones(15)./15^2;
convimg=conv2(doubleCircuit,avarageM,'same');
subplot(2,3,2);
imshow(uint8(convimg));
%---

fftofimage=fft2(doubleCircuit,678,906);
s=log10(1+(fftshift(fftofimage)));
subplot(2,3,3);
imshow(abs(s),[]);

fftofavarege=fft2(avarageM,678,906);
s1=log10(1+(fftshift(fftofavarege)));
subplot(2,3,4);
imshow(abs(s1),[]);

resultoffiltering=fftofimage.*fftofavarege;
s2=log10(1+fftshift(resultoffiltering));
subplot(2,3,5);
imshow(abs(s2),[]);

inverseofimage=ifft2(resultoffiltering,678,906,'symmetric');
subplot(2,3,6);
imshow(uint8(inverseofimage),[]);
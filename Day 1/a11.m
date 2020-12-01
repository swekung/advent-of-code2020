file = uiimport('input.txt');
tStart = cputime;
sums = zeros(200,200);
for i = 1:200
    for j = 1+i:200
        sums(i,j) = file.input(i) + file.input(j);
    end
end
found = 0;
for i = 1:200
    for j = 1+i:200
        if sums(i,j) == 2020
           found = 1;
           break
        end
    end
    if found == 1
        break
    end
end
file.input(i) * file.input(j)
sums = zeros(200,200,200);
for i = 1:200
    for j = 1+i:200
        for k = 1+j:200
            sums(i,j,k) = file.input(i) + file.input(j) + file.input(k);
        end
    end
end
found = 0;
for i = 1:200
    for j = 1+i:200
        for k = 1+j:200
            if sums(i,j,k) == 2020
                found = 1;
                break
            end
        end
        if found == 1
            break
        end
    end
    if found == 1
        break
    end
end
file.input(i) * file.input(j) * file.input(k)
tEnd = cputime - tStart
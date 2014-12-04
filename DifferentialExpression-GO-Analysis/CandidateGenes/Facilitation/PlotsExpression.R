#!/usr/bin/Rscript

args <- commandArgs(TRUE)
File1 = args[1]
File2 = args[2]
PDF = args[3]


pdf(PDF)

Sp1 <- read.csv(File1)
Sp1$new <- ifelse(Sp1$Function == 'BiotinB7', 0.4, ifelse(Sp1$Function == 'CobalaminB12', 0.9, ifelse(Sp1$Function == 'Glucose', 1.4, ifelse(Sp1$Function == 'Mannose', 1.9, ifelse(Sp1$Function == 'Succinate', 2.4, ifelse(Sp1$Function == 'ThiamineB1', 2.9, NaN))))))
#Sp1$cols <- ifelse(x$FDR <= 0.05, ifelse(abs(x$logFC) >= 1, 19, 1), 1)
Sp1$cols <- ifelse(Sp1$FDR <= 0.05, 19, 1)

Sp2 <- read.csv(File2)
Sp2$new <- ifelse(Sp2$Function == 'BiotinB7', 0.6, ifelse(Sp2$Function == 'CobalaminB12', 1.1, ifelse(Sp2$Function == 'Glucose', 1.6, ifelse(Sp2$Function == 'Mannose', 2.1, ifelse(Sp2$Function == 'Succinate', 2.4, ifelse(Sp2$Function == 'ThiamineB1', 3.1, NaN))))))
#Sp2$char <- ifelse(x$FDR <= 0.05, ifelse(abs(x$logFC) >= 1, 19, 1), 1)
Sp2$char <- ifelse(Sp2$FDR <= 0.05, 19, 1)


YupperLim <- ceiling(max(c(abs(Sp1$logFC), abs(Sp2$logFC)))) * -1
YlowerLim <- ceiling(max(c(abs(Sp1$logFC), abs(Sp2$logFC))))

plot(Sp1$new, Sp1$logFC, pch=Sp1$cols, xlim=c(0,6), ylim=c(YlowerLim, YupperLim))
points(Sp2$new, Sp2$logFC, pch=Sp2$char)
abline(h=0, col='gray')

dev.off()

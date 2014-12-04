#!/usr/bin/Rscript

args <- commandArgs(TRUE)
File1 = args[1]
File2 = args[2]
PDF = args[3]


pdf(PDF)

Sp1 <- read.csv(File1)
Sp1$new <- ifelse(Sp1$Function == 'CarbonicAnhydrase', 0.4, ifelse(Sp1$Function == 'GlutamateSemialdehydeAmintransferase', 0.9, ifelse(Sp1$Function == 'IronPermease', 1.4, ifelse(Sp1$Function == 'LHCAB', 1.9, ifelse(Sp1$Function == 'LowAffinityPhosphateTransporter', 2.4, ifelse(Sp1$Function == 'NitrateReductase', 2.9, ifelse(Sp1$Function == 'NitrateTransporter', 3.4, ifelse(Sp1$Function == 'NitriteReductase', 3.9, ifelse(Sp1$Function == 'NitriteTransporter', 4.4, ifelse(Sp1$Function == 'NitrogenAssimilationRegulatoryProtein', 4.9, ifelse(Sp1$Function == 'NitrogenRegulatoryProtein', 5.4, ifelse(Sp1$Function == 'PhosphateTransporter', 5.9, NaN))))))))))))
#Sp1$cols <- ifelse(x$FDR <= 0.05, ifelse(abs(x$logFC) >= 1, 19, 1), 1)
Sp1$cols <- ifelse(Sp1$FDR <= 0.05, 19, 1)





Sp2 <- read.csv(File2)
Sp2$new <- ifelse(Sp2$Function == 'CarbonicAnhydrase', 0.6, ifelse(Sp2$Function == 'GlutamateSemialdehydeAmintransferase', 1.1, ifelse(Sp2$Function == 'IronPermease', 1.6, ifelse(Sp2$Function == 'LHCAB', 2.1, ifelse(Sp2$Function == 'LowAffinityPhosphateTransporter', 2.6, ifelse(Sp2$Function == 'NitrateReductase', 3.1, ifelse(Sp2$Function == 'NitrateTransporter', 3.6, ifelse(Sp2$Function == 'NitriteReductase', 4.1, ifelse(Sp2$Function == 'NitriteTransporter', 4.6, ifelse(Sp2$Function == 'NitrogenAssimilationRegulatoryProtein', 5.1, ifelse(Sp2$Function == 'NitrogenRegulatoryProtein', 5.6, ifelse(Sp2$Function == 'PhosphateTransporter', 6.1, NaN))))))))))))
#Sp2$char <- ifelse(x$FDR <= 0.05, ifelse(abs(x$logFC) >= 1, 19, 1), 1)
Sp2$char <- ifelse(Sp2$FDR <= 0.05, 15, 0)


YupperLim <- ceiling(max(c(abs(Sp1$logFC), abs(Sp2$logFC)))) * -1
YlowerLim <- ceiling(max(c(abs(Sp1$logFC), abs(Sp2$logFC))))

plot(Sp1$new, Sp1$logFC, pch=Sp1$cols, xlim=c(0,6), ylim=c(YlowerLim, YupperLim))
points(Sp2$new, Sp2$logFC, pch=Sp2$char)
abline(h=0, col='gray')

dev.off()

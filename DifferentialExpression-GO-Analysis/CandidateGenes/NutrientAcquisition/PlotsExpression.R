#!/usr/bin/Rscript

args <- commandArgs(TRUE)
File1 = args[1]
File2 = args[2]
PDF = args[3]


pdf(PDF)

# Read in file one of the pair of DE files and format for plotting
Sp1 <- read.csv(File1)
Sp1$new <- ifelse(Sp1$Function == 'CarbonicAnhydrase', 0.4, 
                ifelse(Sp1$Function == 'GlutamateSemialdehydeAmintransferase', 0.9, 
                ifelse(Sp1$Function == 'IronPermease', 1.4, 
                ifelse(Sp1$Function == 'LHCAB', 1.9, 
                ifelse(Sp1$Function == 'LowAffinityPhosphateTransporter', 2.4, 
                ifelse(Sp1$Function == 'NitrateReductase', 2.9, 
                ifelse(Sp1$Function == 'NitrateTransporter', 3.4, 
                ifelse(Sp1$Function == 'NitriteReductase', 3.9, 
                ifelse(Sp1$Function == 'NitriteTransporter', 4.4, 
                ifelse(Sp1$Function == 'NitrogenAssimilationRegulatoryProtein', 4.9, 
                ifelse(Sp1$Function == 'NitrogenRegulatoryProtein', 5.4, 
                ifelse(Sp1$Function == 'PhosphateTransporter', 5.9, 
                    NaN))))))))))))
Sp1$cols <- ifelse(Sp1$FDR <= 0.05, 19, 1)

# Read in file two of the pair of DE files and format for plotting
Sp2 <- read.csv(File2)
Sp2$new <- ifelse(Sp2$Function == 'CarbonicAnhydrase', 0.6, 
                ifelse(Sp2$Function == 'GlutamateSemialdehydeAmintransferase', 1.1, 
                ifelse(Sp2$Function == 'IronPermease', 1.6, ifelse(Sp2$Function == 'LHCAB', 2.1, 
                ifelse(Sp2$Function == 'LowAffinityPhosphateTransporter', 2.6, 
                ifelse(Sp2$Function == 'NitrateReductase', 3.1, 
                ifelse(Sp2$Function == 'NitrateTransporter', 3.6, 
                ifelse(Sp2$Function == 'NitriteReductase', 4.1, 
                ifelse(Sp2$Function == 'NitriteTransporter', 4.6, 
                ifelse(Sp2$Function == 'NitrogenAssimilationRegulatoryProtein', 5.1, 
                ifelse(Sp2$Function == 'NitrogenRegulatoryProtein', 5.6, 
                ifelse(Sp2$Function == 'PhosphateTransporter', 6.1, 
                    NaN))))))))))))
Sp2$char <- ifelse(Sp2$FDR <= 0.05, 15, 0)

# Define the upper and lower limits of the Y axis
LogFCupperLim <- ceiling(max(c(abs(Sp1$logFC), abs(Sp2$logFC)))) 
LogFClowerLim <- ceiling(max(c(abs(Sp1$logFC), abs(Sp2$logFC)))) * -1

# Labels to stick on the X axis
Labels=c('CarbAnhydr', 
         'GSA', 
         'IronPerm', 
         'LHCAB', 
         'LowAPhTrans', 
         'NO3Reduct', 
         'NO3Trans', 
         'NO2Reduct', 
         'NO2Trans', 
         'NitAssRegPr', 
         'NitRegPr', 
         'PhosTrans')

# scatterplot...
par(las=3)

plot(Sp1$new, Sp1$logFC, pch=Sp1$cols, xlim=c(0,6), ylim=c(LogFClowerLim, LogFCupperLim), xaxt='n', xlab='', ylab='logFC')
points(Sp2$new, Sp2$logFC, pch=Sp2$char)
abline(h=0, col='gray')
axis(1,at=seq(from=0.5, to=6, by=0.5),labels=Labels)

dev.off()

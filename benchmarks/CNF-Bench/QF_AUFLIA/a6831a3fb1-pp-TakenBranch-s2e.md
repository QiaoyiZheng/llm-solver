(⟦(= λ1 (= BOPCODE_S2E_INIT 10))⟧) ∧
(⟦(= λ2 (= BOPCODE_S2E_INIT 11))⟧) ∧
(⟦(= λ3 (plus 4 PC_S2I_INIT))⟧) ∧
(⟦(= λ4 (plus 4 λ3))⟧) ∧
(⟦(= λ5 (ite BBUBBLE_S2R_INIT false true))⟧) ∧
(⟦(= λ6 (SRC1_OF AINST_S2R_INIT))⟧) ∧
(⟦(= λ7 (= λ6 BDEST_S2E_INIT))⟧) ∧
(⟦(= λ8 (SRC2_OF AINST_S2R_INIT))⟧) ∧
(⟦(= λ9 (= λ8 BDEST_S2E_INIT))⟧) ∧
(⟦(= λ10 (SRC1_OF BINST_S2R_INIT))⟧) ∧
(⟦(= λ11 (= λ10 BDEST_S2E_INIT))⟧) ∧
(⟦(= λ12 (SRC2_OF BINST_S2R_INIT))⟧) ∧
(⟦(= λ13 (= λ12 BDEST_S2E_INIT))⟧) ∧
(⟦(= λ14 (select IMEM_INIT PC_S2I_INIT))⟧) ∧
(⟦(= λ15 (OPCODE_OF λ14))⟧) ∧
(⟦(= λ16 (select IMEM_INIT λ3))⟧) ∧
(⟦(= λ17 (OPCODE_OF λ16))⟧) ∧
(⟦(= λ18 (DEST_OF λ14))⟧) ∧
(⟦(= λ19 (SRC1_OF λ16))⟧) ∧
(⟦(= λ20 (SRC2_OF λ16))⟧) ∧
(⟦(= λ21 (= λ15 14))⟧) ∧
(⟦(= λ22 (OPCODE_OF BINST_S2R_INIT))⟧) ∧
(⟦(= λ23 (= λ22 10))⟧) ∧
(⟦(= λ24 (DEST_OF BINST_S2R_INIT))⟧) ∧
(⟦(= λ25 (ite CLOCK_INIT NON_DET_STALL_INIT NONDET_MEMSTALL_S1_INIT))⟧) ∧
(⟦(= λ26 (ite λ25 false true))⟧) ∧
(⟦(= λ27 (ite CLOCK_INIT false true))⟧) ∧
(⟦(= λ28 (ite λ27 false true))⟧) ∧
(⟦(= λ29 (ite λ28 false true))⟧) ∧
(⟦(= λ30 (ite λ29 false true))⟧) ∧
(⟦(= λ31 (ite λ30 false true))⟧) ∧
(⟦(= λ32 (ite λ31 false true))⟧) ∧
(⟦(= λ33 (ite λ32 false true))⟧) ∧
(⟦(= λ34 (ite λ33 false true))⟧) ∧
(⟦(= λ35 (ite λ34 false true))⟧) ∧
(⟦(= λ36 (ite λ35 false true))⟧) ∧
(⟦(= λ37 (ite λ36 false true))⟧) ∧
(⟦(= λ38 (ite λ37 false true))⟧) ∧
(⟦(= λ39 (ite CLOCK_INIT false NONDET_MEMSTALL_S1_INIT))⟧) ∧
(⟦(= λ40 (ite λ27 false λ39))⟧) ∧
(⟦(= λ41 (ite λ28 false λ40))⟧) ∧
(⟦(= λ42 (ite λ29 false λ41))⟧) ∧
(⟦(= λ43 (ite λ30 false λ42))⟧) ∧
(⟦(= λ44 (ite λ31 false λ43))⟧) ∧
(⟦(= λ45 (ite λ32 false λ44))⟧) ∧
(⟦(= λ46 (ite λ33 false λ45))⟧) ∧
(⟦(= λ47 (ite λ34 false λ46))⟧) ∧
(⟦(= λ48 (ite λ35 false λ47))⟧) ∧
(⟦(= λ49 (ite (ite λ36 false λ48) false true))⟧) ∧
(⟦(= λ50 (ite λ38 λ49 false))⟧) ∧
(⟦(= λ51 (ite CLOCK_INIT true STALL_S1R_INIT))⟧) ∧
(⟦(= λ52 (ite λ27 true λ51))⟧) ∧
(⟦(= λ53 (ite λ28 true λ52))⟧) ∧
(⟦(= λ54 (ite λ29 true λ53))⟧) ∧
(⟦(= λ55 (ite λ30 true λ54))⟧) ∧
(⟦(= λ56 (ite λ31 true λ55))⟧) ∧
(⟦(= λ57 (ite λ32 true λ56))⟧) ∧
(⟦(= λ58 (ite λ33 true λ57))⟧) ∧
(⟦(= λ59 (ite λ34 true λ58))⟧) ∧
(⟦(= λ60 (ite λ35 true λ59))⟧) ∧
(⟦(= λ61 (ite λ48 false true))⟧) ∧
(⟦(= λ62 (ite λ37 λ61 false))⟧) ∧
(⟦(= λ63 (ite λ47 false true))⟧) ∧
(⟦(= λ64 (ite λ36 λ63 false))⟧) ∧
(⟦(= λ65 (ite λ46 false true))⟧) ∧
(⟦(= λ66 (ite λ35 λ65 false))⟧) ∧
(⟦(= λ67 (ite λ45 false true))⟧) ∧
(⟦(= λ68 (ite λ34 λ67 false))⟧) ∧
(⟦(= λ69 (ite λ44 false true))⟧) ∧
(⟦(= λ70 (ite λ33 λ69 false))⟧) ∧
(⟦(= λ71 (ite λ43 false true))⟧) ∧
(⟦(= λ72 (ite λ32 λ71 false))⟧) ∧
(⟦(= λ73 (ite λ42 false true))⟧) ∧
(⟦(= λ74 (ite λ31 λ73 false))⟧) ∧
(⟦(= λ75 (ite λ41 false true))⟧) ∧
(⟦(= λ76 (ite λ30 λ75 false))⟧) ∧
(⟦(= λ77 (ite λ40 false true))⟧) ∧
(⟦(= λ78 (ite λ29 λ77 false))⟧) ∧
(⟦(= λ79 (ite λ39 false true))⟧) ∧
(⟦(= λ80 (ite λ28 λ79 false))⟧) ∧
(⟦(= λ81 (ite NONDET_MEMSTALL_S1_INIT false true))⟧) ∧
(⟦(= λ82 (ite λ27 λ81 false))⟧) ∧
(⟦(= λ83 (= AOPCODE_S1E_INIT 13))⟧) ∧
(⟦(= λ84 (= ASBYPASSSEL_S1E_INIT 4))⟧) ∧
(⟦(= λ85 (ite (= ASBYPASSSEL_S1E_INIT 0) 0 (ite (= ASBYPASSSEL_S1E_INIT 2) BDATA_S1M_INIT (ite (= ASBYPASSSEL_S1E_INIT 1) ADATA_S1M_INIT (ite (ite λ84 BWASLOAD_S1W_INIT false) BLOADDATA_S1W_INIT (ite λ84 BDATA_S1W_INIT (ite (= ASBYPASSSEL_S1E_INIT 3) ADATA_S1W_INIT ASDATA_S1E_INIT)))))))⟧) ∧
(⟦(= λ86 (= ATBYPASSSEL_S1E_INIT 4))⟧) ∧
(⟦(= λ87 (ite (= ATBYPASSSEL_S1E_INIT 0) 0 (ite (= ATBYPASSSEL_S1E_INIT 2) BDATA_S1M_INIT (ite (= ATBYPASSSEL_S1E_INIT 1) ADATA_S1M_INIT (ite (ite λ86 BWASLOAD_S1W_INIT false) BLOADDATA_S1W_INIT (ite λ86 BDATA_S1W_INIT (ite (= ATBYPASSSEL_S1E_INIT 3) ADATA_S1W_INIT ATDATA_S1E_INIT)))))))⟧) ∧
(⟦(= λ88 (ite (ite TAKENBRANCH_S1M_INIT false true) (ite (ite STALL_S1E_INIT false true) (ite (= AOPCODE_S1E_INIT 12) true (ite (= AOPCODE_S1E_INIT 14) true (ite λ83 true (ite (= AOPCODE_S1E_INIT 15) (BRANCH_CONDITION λ85 λ87) false)))) false) false))⟧) ∧
(⟦(= λ89 (ite λ83 λ85 ATARGET_S1E_INIT))⟧) ∧
(⟦(= λ90 (ite λ88 λ89 PC_PLUS_S2I_INIT))⟧) ∧
(⟦(= λ91 (ite λ82 (ite STALL_S1R_INIT PC_S2I_INIT λ90) PC_S2I_INIT))⟧) ∧
(⟦(= λ92 (ite CLOCK_INIT TAKENBRANCH_S2E_INIT TAKENBRANCH_S1M_INIT))⟧) ∧
(⟦(= λ93 (ite CLOCK_INIT STALL_S2R_INIT STALL_S1E_INIT))⟧) ∧
(⟦(= λ94 (OPCODE_OF AINST_S2R_INIT))⟧) ∧
(⟦(= λ95 (ite CLOCK_INIT λ94 AOPCODE_S1E_INIT))⟧) ∧
(⟦(= λ96 (= λ95 13))⟧) ∧
(⟦(= λ97 (ite CLOCK_INIT (ite (= λ6 0) 0 (ite λ7 2 (ite (= λ6 ADEST_S2E_INIT) 1 (ite (= λ6 BDEST_S2M_INIT) 4 (ite (= λ6 ADEST_S2M_INIT) 3 5))))) ASBYPASSSEL_S1E_INIT))⟧) ∧
(⟦(= λ98 (ite (ite INSTRISLOAD_S2E_INIT true INSTRISSTORE_S2E_INIT) (plus BSBUS_S2E_INIT BSRC2BUS_S2E_INIT) (ALU (ALU_OP_OF BOPCODE_S2E_INIT) BSBUS_S2E_INIT BSRC2BUS_S2E_INIT)))⟧) ∧
(⟦(= λ99 (ite CLOCK_INIT λ98 BDATA_S1M_INIT))⟧) ∧
(⟦(= λ100 (ite CLOCK_INIT (ite PCDRVRESULT_S2E_INIT PCPLUS_S2R_INIT (ALU (ALU_OP_OF AOPCODE_S2E_INIT) ASBUS_S2E_INIT ASRC2BUS_S2E_INIT)) ADATA_S1M_INIT))⟧) ∧
(⟦(= λ101 (= λ97 4))⟧) ∧
(⟦(= λ102 (ite CLOCK_INIT INSTRISLOAD_S2M_INIT BWASLOAD_S1W_INIT))⟧) ∧
(⟦(= λ103 (ite (ite INSTRISLOAD_S2M_INIT CLOCK_INIT false) (ite INSTRISLOAD_S2M_INIT CACHEDOUT_S2_INIT NO_VALUE0) BLOADDATA_S1W_INIT))⟧) ∧
(⟦(= λ104 (ite CLOCK_INIT BDATA_S2M_INIT BDATA_S1W_INIT))⟧) ∧
(⟦(= λ105 (ite CLOCK_INIT ADATA_S2M_INIT ADATA_S1W_INIT))⟧) ∧
(⟦(= λ106 (ite CLOCK_INIT (select REGFILE_INIT λ6) ASDATA_S1E_INIT))⟧) ∧
(⟦(= λ107 (ite (= λ97 0) 0 (ite (= λ97 2) λ99 (ite (= λ97 1) λ100 (ite (ite λ101 λ102 false) λ103 (ite λ101 λ104 (ite (= λ97 3) λ105 λ106)))))))⟧) ∧
(⟦(= λ108 (ite CLOCK_INIT (ite (= λ8 0) 0 (ite λ9 2 (ite (= λ8 ADEST_S2E_INIT) 1 (ite (= λ8 BDEST_S2M_INIT) 4 (ite (= λ8 ADEST_S2M_INIT) 3 5))))) ATBYPASSSEL_S1E_INIT))⟧) ∧
(⟦(= λ109 (= λ108 4))⟧) ∧
(⟦(= λ110 (ite CLOCK_INIT (select REGFILE_INIT λ8) ATDATA_S1E_INIT))⟧) ∧
(⟦(= λ111 (ite (= λ108 0) 0 (ite (= λ108 2) λ99 (ite (= λ108 1) λ100 (ite (ite λ109 λ102 false) λ103 (ite λ109 λ104 (ite (= λ108 3) λ105 λ110)))))))⟧) ∧
(⟦(= λ112 (ite (ite λ92 false true) (ite (ite λ93 false true) (ite (= λ95 12) true (ite (= λ95 14) true (ite λ96 true (ite (= λ95 15) (BRANCH_CONDITION λ107 λ111) false)))) false) false))⟧) ∧
(⟦(= λ113 (ite λ96 λ107 (plus (OFFSET_OF AINST_S2R_INIT) (plus 4 PC_CHAIN_S2R_INIT))))⟧) ∧
(⟦(= λ114 (ite λ82 (ite STALL_S1R_INIT λ90 (ite λ88 (plus 4 (plus 4 λ89)) (plus 4 (plus 4 PC_PLUS_S2I_INIT)))) PC_PLUS_S2I_INIT))⟧) ∧
(⟦(= λ115 (ite λ112 λ113 λ114))⟧) ∧
(⟦(= λ116 (ite λ80 (ite λ51 λ91 λ115) λ91))⟧) ∧
(⟦(= λ117 (ite λ82 false true))⟧) ∧
(⟦(= λ118 (ite λ117 TAKENBRANCH_S2E_INIT (ite STALL_S1E_INIT TAKENBRANCH_S2E_INIT λ88)))⟧) ∧
(⟦(= λ119 (ite λ27 λ118 λ92))⟧) ∧
(⟦(= λ120 (ite λ81 λ27 false))⟧) ∧
(⟦(= λ121 (ite λ120 STALL_S1R_INIT STALL_S2R_INIT))⟧) ∧
(⟦(= λ122 (ite λ27 λ121 λ93))⟧) ∧
(⟦(= λ123 (ite STALL_S1R_INIT true λ117))⟧) ∧
(⟦(= λ124 (ite λ123 AINST_S2R_INIT AINST_S1R_INIT))⟧) ∧
(⟦(= λ125 (OPCODE_OF λ124))⟧) ∧
(⟦(= λ126 (ite λ27 λ125 λ95))⟧) ∧
(⟦(= λ127 (= λ126 13))⟧) ∧
(⟦(= λ128 (SRC1_OF λ124))⟧) ∧
(⟦(= λ129 (ite λ117 BDEST_S2E_INIT (ite BBUBBLE_S1E_INIT 0 BDEST_S1E_INIT)))⟧) ∧
(⟦(= λ130 (ite λ117 ADEST_S2E_INIT ADEST_S1E_INIT))⟧) ∧
(⟦(= λ131 (ite λ117 BDEST_S2M_INIT BDEST_S1M_INIT))⟧) ∧
(⟦(= λ132 (ite λ117 ADEST_S2M_INIT ADEST_S1M_INIT))⟧) ∧
(⟦(= λ133 (ite λ27 (ite (= λ128 0) 0 (ite (= λ129 λ128) 2 (ite (= λ130 λ128) 1 (ite (= λ131 λ128) 4 (ite (= λ132 λ128) 3 5))))) λ97))⟧) ∧
(⟦(= λ134 (ite λ117 INSTRISLOAD_S2E_INIT INSTRISLOAD_S1E_INIT))⟧) ∧
(⟦(= λ135 (ite λ117 INSTRISSTORE_S2E_INIT INSTRISSTORE_S1E_INIT))⟧) ∧
(⟦(= λ136 (= BSBYPASSSEL_S1E_INIT 4))⟧) ∧
(⟦(= λ137 (ite λ117 BSBUS_S2E_INIT (ite (= BSBYPASSSEL_S1E_INIT 0) 0 (ite (= BSBYPASSSEL_S1E_INIT 2) BDATA_S1M_INIT (ite (= BSBYPASSSEL_S1E_INIT 1) ADATA_S1M_INIT (ite (ite λ136 BWASLOAD_S1W_INIT false) BLOADDATA_S1W_INIT (ite λ136 BDATA_S1W_INIT (ite (= BSBYPASSSEL_S1E_INIT 3) ADATA_S1W_INIT BSDATA_S1E_INIT))))))))⟧) ∧
(⟦(= λ138 (= BTBYPASSSEL_S1E_INIT 4))⟧) ∧
(⟦(= λ139 (ite (= BTBYPASSSEL_S1E_INIT 0) 0 (ite (= BTBYPASSSEL_S1E_INIT 2) BDATA_S1M_INIT (ite (= BTBYPASSSEL_S1E_INIT 1) ADATA_S1M_INIT (ite (ite λ138 BWASLOAD_S1W_INIT false) BLOADDATA_S1W_INIT (ite λ138 BDATA_S1W_INIT (ite (= BTBYPASSSEL_S1E_INIT 3) ADATA_S1W_INIT BTDATA_S1E_INIT)))))))⟧) ∧
(⟦(= λ140 (ite λ117 BSRC2BUS_S2E_INIT (ite BUSEIMM_S1E_INIT BIMMBUS_S1E_INIT λ139)))⟧) ∧
(⟦(= λ141 (ite λ117 BOPCODE_S2E_INIT BOPCODE_S1E_INIT))⟧) ∧
(⟦(= λ142 (ite (ite λ134 true λ135) (plus λ137 λ140) (ALU (ALU_OP_OF λ141) λ137 λ140)))⟧) ∧
(⟦(= λ143 (ite λ27 λ142 λ99))⟧) ∧
(⟦(= λ144 (ite λ117 PCDRVRESULT_S2E_INIT PCDRVRESULT_S1E_INIT))⟧) ∧
(⟦(= λ145 (ite λ120 PCPLUS_S1R_INIT PCPLUS_S2R_INIT))⟧) ∧
(⟦(= λ146 (ite λ117 AOPCODE_S2E_INIT AOPCODE_S1E_INIT))⟧) ∧
(⟦(= λ147 (ite λ117 ASBUS_S2E_INIT λ85))⟧) ∧
(⟦(= λ148 (ite λ117 ASRC2BUS_S2E_INIT (ite AUSEIMM_S1E_INIT AIMMBUS_S1E_INIT λ87)))⟧) ∧
(⟦(= λ149 (ite λ27 (ite λ144 λ145 (ALU (ALU_OP_OF λ146) λ147 λ148)) λ100))⟧) ∧
(⟦(= λ150 (= λ133 4))⟧) ∧
(⟦(= λ151 (ite λ82 INSTRISLOAD_S1M_INIT INSTRISLOAD_S2M_INIT))⟧) ∧
(⟦(= λ152 (ite λ27 λ151 λ102))⟧) ∧
(⟦(= λ153 (ite (ite λ27 (ite INSTRISSTORE_S1M_INIT λ81 false) false) (store DMEM_INIT STOREADDR_S1M_INIT STOREDATA_S1M_INIT) DMEM_INIT))⟧) ∧
(⟦(= λ154 (ite λ27 (select λ153 (ite (ite INSTRISLOAD_S1M_INIT λ81 false) MEMADDR_S1M_INIT MISSADDR_S1W_INIT)) CACHEDOUT_S2_INIT))⟧) ∧
(⟦(= λ155 (ite (ite λ151 λ27 false) (ite λ151 λ154 NO_VALUE1) λ103))⟧) ∧
(⟦(= λ156 (ite λ117 BDATA_S2M_INIT BDATA_S1M_INIT))⟧) ∧
(⟦(= λ157 (ite λ27 λ156 λ104))⟧) ∧
(⟦(= λ158 (ite λ117 ADATA_S2M_INIT ADATA_S1M_INIT))⟧) ∧
(⟦(= λ159 (ite λ27 λ158 λ105))⟧) ∧
(⟦(= λ160 (ite (ite (ite (= ADEST_S1W_INIT 0) false true) λ82 false) (store REGFILE_INIT ADEST_S1W_INIT ADATA_S1W_INIT) REGFILE_INIT))⟧) ∧
(⟦(= λ161 (ite (ite (ite (= BDEST_S1W_INIT 0) false true) λ82 false) (store λ160 BDEST_S1W_INIT (ite BWASLOAD_S1W_INIT BLOADDATA_S1W_INIT BDATA_S1W_INIT)) λ160))⟧) ∧
(⟦(= λ162 (ite λ27 (select λ161 λ128) λ106))⟧) ∧
(⟦(= λ163 (ite (= λ133 0) 0 (ite (= λ133 2) λ143 (ite (= λ133 1) λ149 (ite (ite λ150 λ152 false) λ155 (ite λ150 λ157 (ite (= λ133 3) λ159 λ162)))))))⟧) ∧
(⟦(= λ164 (SRC2_OF λ124))⟧) ∧
(⟦(= λ165 (ite λ27 (ite (= λ164 0) 0 (ite (= λ164 λ129) 2 (ite (= λ164 λ130) 1 (ite (= λ164 λ131) 4 (ite (= λ164 λ132) 3 5))))) λ108))⟧) ∧
(⟦(= λ166 (= λ165 4))⟧) ∧
(⟦(= λ167 (ite λ27 (select λ161 λ164) λ110))⟧) ∧
(⟦(= λ168 (ite (= λ165 0) 0 (ite (= λ165 2) λ143 (ite (= λ165 1) λ149 (ite (ite λ166 λ152 false) λ155 (ite λ166 λ157 (ite (= λ165 3) λ159 λ167)))))))⟧) ∧
(⟦(= λ169 (ite (ite λ119 false true) (ite (ite λ122 false true) (ite (= λ126 12) true (ite (= λ126 14) true (ite λ127 true (ite (= λ126 15) (BRANCH_CONDITION λ163 λ168) false)))) false) false))⟧) ∧
(⟦(= λ170 (ite λ120 PC_CHAIN_S1R_INIT PC_CHAIN_S2R_INIT))⟧) ∧
(⟦(= λ171 (ite λ127 λ163 (plus (OFFSET_OF λ124) (plus 4 λ170))))⟧) ∧
(⟦(= λ172 (ite λ112 (plus 4 (plus 4 λ113)) (plus 4 (plus 4 λ114))))⟧) ∧
(⟦(= λ173 (ite λ80 (ite λ51 λ115 λ172) λ114))⟧) ∧
(⟦(= λ174 (ite λ169 λ171 λ173))⟧) ∧
(⟦(= λ175 (ite λ78 (ite λ52 λ116 λ174) λ116))⟧) ∧
(⟦(= λ176 (ite λ80 false true))⟧) ∧
(⟦(= λ177 (ite λ93 λ118 λ112))⟧) ∧
(⟦(= λ178 (ite λ176 λ118 λ177))⟧) ∧
(⟦(= λ179 (ite λ28 λ178 λ119))⟧) ∧
(⟦(= λ180 (ite λ79 λ28 false))⟧) ∧
(⟦(= λ181 (ite λ180 λ51 λ121))⟧) ∧
(⟦(= λ182 (ite λ28 λ181 λ122))⟧) ∧
(⟦(= λ183 (ite λ51 true λ176))⟧) ∧
(⟦(= λ184 (ite CLOCK_INIT λ14 AINST_S1R_INIT))⟧) ∧
(⟦(= λ185 (ite λ183 λ124 λ184))⟧) ∧
(⟦(= λ186 (OPCODE_OF λ185))⟧) ∧
(⟦(= λ187 (ite λ28 λ186 λ126))⟧) ∧
(⟦(= λ188 (= λ187 13))⟧) ∧
(⟦(= λ189 (SRC1_OF λ185))⟧) ∧
(⟦(= λ190 (ite CLOCK_INIT BBUBBLE_S2R_INIT BBUBBLE_S1E_INIT))⟧) ∧
(⟦(= λ191 (= λ22 16))⟧) ∧
(⟦(= λ192 (= λ22 17))⟧) ∧
(⟦(= λ193 (ite CLOCK_INIT (ite BBUBBLE_S2R_INIT 0 (ite (ite (ite λ191 false (ite λ23 true λ192)) true λ191) λ24 0)) BDEST_S1E_INIT))⟧) ∧
(⟦(= λ194 (ite λ190 0 λ193))⟧) ∧
(⟦(= λ195 (ite λ176 λ129 λ194))⟧) ∧
(⟦(= λ196 (= λ94 16))⟧) ∧
(⟦(= λ197 (= λ94 17))⟧) ∧
(⟦(= λ198 (= λ94 14))⟧) ∧
(⟦(= λ199 (ite CLOCK_INIT (ite ABUBBLE_S2R_INIT 0 (ite (ite λ196 false (ite λ197 false (ite λ198 (ite TAKENBRANCH_S2E_INIT false true) false))) 31 (ite (ite (ite λ196 false λ197) true λ196) (DEST_OF AINST_S2R_INIT) 0))) ADEST_S1E_INIT))⟧) ∧
(⟦(= λ200 (ite λ176 λ130 λ199))⟧) ∧
(⟦(= λ201 (ite CLOCK_INIT BDEST_S2E_INIT BDEST_S1M_INIT))⟧) ∧
(⟦(= λ202 (ite λ176 λ131 λ201))⟧) ∧
(⟦(= λ203 (ite CLOCK_INIT ADEST_S2E_INIT ADEST_S1M_INIT))⟧) ∧
(⟦(= λ204 (ite λ176 λ132 λ203))⟧) ∧
(⟦(= λ205 (ite λ28 (ite (= λ189 0) 0 (ite (= λ195 λ189) 2 (ite (= λ200 λ189) 1 (ite (= λ202 λ189) 4 (ite (= λ204 λ189) 3 5))))) λ133))⟧) ∧
(⟦(= λ206 (ite CLOCK_INIT (ite λ23 λ5 false) INSTRISLOAD_S1E_INIT))⟧) ∧
(⟦(= λ207 (ite λ176 λ134 λ206))⟧) ∧
(⟦(= λ208 (= λ22 11))⟧) ∧
(⟦(= λ209 (ite CLOCK_INIT (ite λ208 λ5 false) INSTRISSTORE_S1E_INIT))⟧) ∧
(⟦(= λ210 (ite λ176 λ135 λ209))⟧) ∧
(⟦(= λ211 (ite CLOCK_INIT (ite (= λ10 0) 0 (ite λ11 2 (ite (= λ10 ADEST_S2E_INIT) 1 (ite (= λ10 BDEST_S2M_INIT) 4 (ite (= λ10 ADEST_S2M_INIT) 3 5))))) BSBYPASSSEL_S1E_INIT))⟧) ∧
(⟦(= λ212 (= λ211 4))⟧) ∧
(⟦(= λ213 (ite CLOCK_INIT (select REGFILE_INIT λ10) BSDATA_S1E_INIT))⟧) ∧
(⟦(= λ214 (ite (= λ211 0) 0 (ite (= λ211 2) λ99 (ite (= λ211 1) λ100 (ite (ite λ212 λ102 false) λ103 (ite λ212 λ104 (ite (= λ211 3) λ105 λ213)))))))⟧) ∧
(⟦(= λ215 (ite λ176 λ137 λ214))⟧) ∧
(⟦(= λ216 (ite CLOCK_INIT (SHORT_IMMED_OF BINST_S2R_INIT) BIMMBUS_S1E_INIT))⟧) ∧
(⟦(= λ217 (ite CLOCK_INIT (ite (= λ12 0) 0 (ite λ13 2 (ite (= λ12 ADEST_S2E_INIT) 1 (ite (= λ12 BDEST_S2M_INIT) 4 (ite (= λ12 ADEST_S2M_INIT) 3 5))))) BTBYPASSSEL_S1E_INIT))⟧) ∧
(⟦(= λ218 (= λ217 4))⟧) ∧
(⟦(= λ219 (ite CLOCK_INIT (select REGFILE_INIT λ12) BTDATA_S1E_INIT))⟧) ∧
(⟦(= λ220 (ite (= λ217 0) 0 (ite (= λ217 2) λ99 (ite (= λ217 1) λ100 (ite (ite λ218 λ102 false) λ103 (ite λ218 λ104 (ite (= λ217 3) λ105 λ219)))))))⟧) ∧
(⟦(= λ221 (ite (ite CLOCK_INIT (ite λ192 true (ite λ23 true λ208)) NO_VALUE2) λ216 λ220))⟧) ∧
(⟦(= λ222 (ite λ176 λ140 λ221))⟧) ∧
(⟦(= λ223 (ite CLOCK_INIT λ22 BOPCODE_S1E_INIT))⟧) ∧
(⟦(= λ224 (ite λ176 λ141 λ223))⟧) ∧
(⟦(= λ225 (ite (ite λ207 true λ210) (plus λ215 λ222) (ALU (ALU_OP_OF λ224) λ215 λ222)))⟧) ∧
(⟦(= λ226 (ite λ28 λ225 λ143))⟧) ∧
(⟦(= λ227 (ite CLOCK_INIT λ198 PCDRVRESULT_S1E_INIT))⟧) ∧
(⟦(= λ228 (ite λ176 λ144 λ227))⟧) ∧
(⟦(= λ229 (ite CLOCK_INIT λ4 PCPLUS_S1R_INIT))⟧) ∧
(⟦(= λ230 (ite λ180 λ229 λ145))⟧) ∧
(⟦(= λ231 (ite λ176 λ146 λ95))⟧) ∧
(⟦(= λ232 (ite λ176 λ147 λ107))⟧) ∧
(⟦(= λ233 (ite CLOCK_INIT λ197 AUSEIMM_S1E_INIT))⟧) ∧
(⟦(= λ234 (ite CLOCK_INIT (SHORT_IMMED_OF AINST_S2R_INIT) AIMMBUS_S1E_INIT))⟧) ∧
(⟦(= λ235 (ite λ233 λ234 λ111))⟧) ∧
(⟦(= λ236 (ite λ176 λ148 λ235))⟧) ∧
(⟦(= λ237 (ite λ28 (ite λ228 λ230 (ALU (ALU_OP_OF λ231) λ232 λ236)) λ149))⟧) ∧
(⟦(= λ238 (= λ205 4))⟧) ∧
(⟦(= λ239 (ite CLOCK_INIT INSTRISLOAD_S2E_INIT INSTRISLOAD_S1M_INIT))⟧) ∧
(⟦(= λ240 (ite λ80 λ239 λ151))⟧) ∧
(⟦(= λ241 (ite λ28 λ240 λ152))⟧) ∧
(⟦(= λ242 (ite CLOCK_INIT INSTRISSTORE_S2E_INIT INSTRISSTORE_S1M_INIT))⟧) ∧
(⟦(= λ243 (ite CLOCK_INIT λ98 STOREADDR_S1M_INIT))⟧) ∧
(⟦(= λ244 (ite CLOCK_INIT STOREDATA_S2E_INIT STOREDATA_S1M_INIT))⟧) ∧
(⟦(= λ245 (store λ153 λ243 λ244))⟧) ∧
(⟦(= λ246 (ite (ite λ28 (ite λ242 λ79 false) false) λ245 λ153))⟧) ∧
(⟦(= λ247 (ite CLOCK_INIT λ98 MEMADDR_S1M_INIT))⟧) ∧
(⟦(= λ248 (ite CLOCK_INIT STOREADDR_S2M_INIT MISSADDR_S1W_INIT))⟧) ∧
(⟦(= λ249 (ite λ28 (select λ246 (ite (ite λ239 λ79 false) λ247 λ248)) λ154))⟧) ∧
(⟦(= λ250 (ite (ite λ240 λ28 false) (ite λ240 λ249 NO_VALUE3) λ155))⟧) ∧
(⟦(= λ251 (ite λ176 λ156 λ99))⟧) ∧
(⟦(= λ252 (ite λ28 λ251 λ157))⟧) ∧
(⟦(= λ253 (ite λ176 λ158 λ100))⟧) ∧
(⟦(= λ254 (ite λ28 λ253 λ159))⟧) ∧
(⟦(= λ255 (ite CLOCK_INIT BDEST_S2M_INIT BDEST_S1W_INIT))⟧) ∧
(⟦(= λ256 (ite (= λ255 0) false true))⟧) ∧
(⟦(= λ257 (ite CLOCK_INIT ADEST_S2M_INIT ADEST_S1W_INIT))⟧) ∧
(⟦(= λ258 (ite (= λ257 0) false true))⟧) ∧
(⟦(= λ259 (store λ161 λ257 λ105))⟧) ∧
(⟦(= λ260 (ite (ite λ258 λ80 false) λ259 λ161))⟧) ∧
(⟦(= λ261 (ite λ102 λ103 λ104))⟧) ∧
(⟦(= λ262 (ite (ite λ256 λ80 false) (store λ260 λ255 λ261) λ260))⟧) ∧
(⟦(= λ263 (ite λ28 (select λ262 λ189) λ162))⟧) ∧
(⟦(= λ264 (ite (= λ205 0) 0 (ite (= λ205 2) λ226 (ite (= λ205 1) λ237 (ite (ite λ238 λ241 false) λ250 (ite λ238 λ252 (ite (= λ205 3) λ254 λ263)))))))⟧) ∧
(⟦(= λ265 (SRC2_OF λ185))⟧) ∧
(⟦(= λ266 (ite λ28 (ite (= λ265 0) 0 (ite (= λ265 λ195) 2 (ite (= λ265 λ200) 1 (ite (= λ265 λ202) 4 (ite (= λ265 λ204) 3 5))))) λ165))⟧) ∧
(⟦(= λ267 (= λ266 4))⟧) ∧
(⟦(= λ268 (ite λ28 (select λ262 λ265) λ167))⟧) ∧
(⟦(= λ269 (ite (= λ266 0) 0 (ite (= λ266 2) λ226 (ite (= λ266 1) λ237 (ite (ite λ267 λ241 false) λ250 (ite λ267 λ252 (ite (= λ266 3) λ254 λ268)))))))⟧) ∧
(⟦(= λ270 (ite (ite λ179 false true) (ite (ite λ182 false true) (ite (= λ187 12) true (ite (= λ187 14) true (ite λ188 true (ite (= λ187 15) (BRANCH_CONDITION λ264 λ269) false)))) false) false))⟧) ∧
(⟦(= λ271 (ite CLOCK_INIT PC_S2I_INIT PC_CHAIN_S1R_INIT))⟧) ∧
(⟦(= λ272 (ite λ180 λ271 λ170))⟧) ∧
(⟦(= λ273 (ite λ188 λ264 (plus (OFFSET_OF λ185) (plus 4 λ272))))⟧) ∧
(⟦(= λ274 (plus 4 (plus 4 λ171)))⟧) ∧
(⟦(= λ275 (ite λ78 (ite λ52 λ174 (ite λ169 λ274 (plus 4 (plus 4 λ173)))) λ173))⟧) ∧
(⟦(= λ276 (ite λ270 λ273 λ275))⟧) ∧
(⟦(= λ277 (ite λ76 (ite λ53 λ175 λ276) λ175))⟧) ∧
(⟦(= λ278 (ite λ78 false true))⟧) ∧
(⟦(= λ279 (ite λ278 λ178 (ite λ122 λ178 λ169)))⟧) ∧
(⟦(= λ280 (ite λ29 λ279 λ179))⟧) ∧
(⟦(= λ281 (ite λ77 λ29 false))⟧) ∧
(⟦(= λ282 (ite λ281 λ52 λ181))⟧) ∧
(⟦(= λ283 (ite λ29 λ282 λ182))⟧) ∧
(⟦(= λ284 (ite λ52 true λ278))⟧) ∧
(⟦(= λ285 (ite λ27 (select IMEM_INIT λ91) λ184))⟧) ∧
(⟦(= λ286 (ite λ284 λ185 λ285))⟧) ∧
(⟦(= λ287 (OPCODE_OF λ286))⟧) ∧
(⟦(= λ288 (ite λ29 λ287 λ187))⟧) ∧
(⟦(= λ289 (= λ288 13))⟧) ∧
(⟦(= λ290 (SRC1_OF λ286))⟧) ∧
(⟦(= λ291 (ite λ120 BBUBBLE_S1R_INIT BBUBBLE_S2R_INIT))⟧) ∧
(⟦(= λ292 (ite λ27 λ291 λ190))⟧) ∧
(⟦(= λ293 (ite λ123 BINST_S2R_INIT BINST_S1R_INIT))⟧) ∧
(⟦(= λ294 (OPCODE_OF λ293))⟧) ∧
(⟦(= λ295 (= λ294 16))⟧) ∧
(⟦(= λ296 (= λ294 10))⟧) ∧
(⟦(= λ297 (= λ294 17))⟧) ∧
(⟦(= λ298 (ite λ27 (ite λ291 0 (ite (ite (ite λ295 false (ite λ296 true λ297)) true λ295) (DEST_OF λ293) 0)) λ193))⟧) ∧
(⟦(= λ299 (ite λ292 0 λ298))⟧) ∧
(⟦(= λ300 (ite λ278 λ195 λ299))⟧) ∧
(⟦(= λ301 (ite λ120 ABUBBLE_S1R_INIT ABUBBLE_S2R_INIT))⟧) ∧
(⟦(= λ302 (= 16 λ125))⟧) ∧
(⟦(= λ303 (= 17 λ125))⟧) ∧
(⟦(= λ304 (= λ125 14))⟧) ∧
(⟦(= λ305 (ite λ27 (ite λ301 0 (ite (ite λ302 false (ite λ303 false (ite λ304 (ite λ118 false true) false))) 31 (ite (ite (ite λ302 false λ303) true λ302) (DEST_OF λ124) 0))) λ199))⟧) ∧
(⟦(= λ306 (ite λ278 λ200 λ305))⟧) ∧
(⟦(= λ307 (ite λ27 λ129 λ201))⟧) ∧
(⟦(= λ308 (ite λ278 λ202 λ307))⟧) ∧
(⟦(= λ309 (ite λ27 λ130 λ203))⟧) ∧
(⟦(= λ310 (ite λ278 λ204 λ309))⟧) ∧
(⟦(= λ311 (ite λ29 (ite (= λ290 0) 0 (ite (= λ300 λ290) 2 (ite (= λ306 λ290) 1 (ite (= λ308 λ290) 4 (ite (= λ310 λ290) 3 5))))) λ205))⟧) ∧
(⟦(= λ312 (ite λ291 false true))⟧) ∧
(⟦(= λ313 (ite λ27 (ite λ296 λ312 false) λ206))⟧) ∧
(⟦(= λ314 (ite λ278 λ207 λ313))⟧) ∧
(⟦(= λ315 (= λ294 11))⟧) ∧
(⟦(= λ316 (ite λ27 (ite λ315 λ312 false) λ209))⟧) ∧
(⟦(= λ317 (ite λ278 λ210 λ316))⟧) ∧
(⟦(= λ318 (SRC1_OF λ293))⟧) ∧
(⟦(= λ319 (ite λ27 (ite (= λ318 0) 0 (ite (= λ318 λ129) 2 (ite (= λ318 λ130) 1 (ite (= λ318 λ131) 4 (ite (= λ318 λ132) 3 5))))) λ211))⟧) ∧
(⟦(= λ320 (= λ319 4))⟧) ∧
(⟦(= λ321 (ite λ27 (select λ161 λ318) λ213))⟧) ∧
(⟦(= λ322 (ite (= λ319 0) 0 (ite (= λ319 2) λ143 (ite (= λ319 1) λ149 (ite (ite λ320 λ152 false) λ155 (ite λ320 λ157 (ite (= λ319 3) λ159 λ321)))))))⟧) ∧
(⟦(= λ323 (ite λ278 λ215 λ322))⟧) ∧
(⟦(= λ324 (ite λ27 (SHORT_IMMED_OF λ293) λ216))⟧) ∧
(⟦(= λ325 (SRC2_OF λ293))⟧) ∧
(⟦(= λ326 (ite λ27 (ite (= λ325 0) 0 (ite (= λ325 λ129) 2 (ite (= λ325 λ130) 1 (ite (= λ325 λ131) 4 (ite (= λ325 λ132) 3 5))))) λ217))⟧) ∧
(⟦(= λ327 (= λ326 4))⟧) ∧
(⟦(= λ328 (ite λ27 (select λ161 λ325) λ219))⟧) ∧
(⟦(= λ329 (ite (= λ326 0) 0 (ite (= λ326 2) λ143 (ite (= λ326 1) λ149 (ite (ite λ327 λ152 false) λ155 (ite λ327 λ157 (ite (= λ326 3) λ159 λ328)))))))⟧) ∧
(⟦(= λ330 (ite (ite λ27 (ite λ297 true (ite λ296 true λ315)) NO_VALUE4) λ324 λ329))⟧) ∧
(⟦(= λ331 (ite λ278 λ222 λ330))⟧) ∧
(⟦(= λ332 (ite λ27 λ294 λ223))⟧) ∧
(⟦(= λ333 (ite λ278 λ224 λ332))⟧) ∧
(⟦(= λ334 (ite (ite λ314 true λ317) (plus λ323 λ331) (ALU (ALU_OP_OF λ333) λ323 λ331)))⟧) ∧
(⟦(= λ335 (ite λ29 λ334 λ226))⟧) ∧
(⟦(= λ336 (ite λ27 λ304 λ227))⟧) ∧
(⟦(= λ337 (ite λ278 λ228 λ336))⟧) ∧
(⟦(= λ338 (plus 4 λ91))⟧) ∧
(⟦(= λ339 (ite λ27 (plus 4 λ338) λ229))⟧) ∧
(⟦(= λ340 (ite λ281 λ339 λ230))⟧) ∧
(⟦(= λ341 (ite λ278 λ231 λ126))⟧) ∧
(⟦(= λ342 (ite λ278 λ232 λ163))⟧) ∧
(⟦(= λ343 (ite λ27 λ303 λ233))⟧) ∧
(⟦(= λ344 (ite λ27 (SHORT_IMMED_OF λ124) λ234))⟧) ∧
(⟦(= λ345 (ite λ343 λ344 λ168))⟧) ∧
(⟦(= λ346 (ite λ278 λ236 λ345))⟧) ∧
(⟦(= λ347 (ite λ29 (ite λ337 λ340 (ALU (ALU_OP_OF λ341) λ342 λ346)) λ237))⟧) ∧
(⟦(= λ348 (= λ311 4))⟧) ∧
(⟦(= λ349 (ite λ27 λ134 λ239))⟧) ∧
(⟦(= λ350 (ite λ78 λ349 λ240))⟧) ∧
(⟦(= λ351 (ite λ29 λ350 λ241))⟧) ∧
(⟦(= λ352 (ite λ27 λ135 λ242))⟧) ∧
(⟦(= λ353 (ite λ27 λ142 λ243))⟧) ∧
(⟦(= λ354 (ite λ117 STOREDATA_S2E_INIT λ139))⟧) ∧
(⟦(= λ355 (ite λ27 λ354 λ244))⟧) ∧
(⟦(= λ356 (ite (ite λ29 (ite λ352 λ77 false) false) (store λ246 λ353 λ355) λ246))⟧) ∧
(⟦(= λ357 (ite λ27 λ142 λ247))⟧) ∧
(⟦(= λ358 (ite λ82 MEMADDR_S1M_INIT STOREADDR_S2M_INIT))⟧) ∧
(⟦(= λ359 (ite λ27 λ358 λ248))⟧) ∧
(⟦(= λ360 (ite λ29 (select λ356 (ite (ite λ349 λ77 false) λ357 λ359)) λ249))⟧) ∧
(⟦(= λ361 (ite (ite λ350 λ29 false) (ite λ350 λ360 NO_VALUE5) λ250))⟧) ∧
(⟦(= λ362 (ite λ278 λ251 λ143))⟧) ∧
(⟦(= λ363 (ite λ29 λ362 λ252))⟧) ∧
(⟦(= λ364 (ite λ278 λ253 λ149))⟧) ∧
(⟦(= λ365 (ite λ29 λ364 λ254))⟧) ∧
(⟦(= λ366 (ite λ27 λ131 λ255))⟧) ∧
(⟦(= λ367 (ite (= λ366 0) false true))⟧) ∧
(⟦(= λ368 (ite λ27 λ132 λ257))⟧) ∧
(⟦(= λ369 (ite (= λ368 0) false true))⟧) ∧
(⟦(= λ370 (ite (ite λ369 λ78 false) (store λ262 λ368 λ159) λ262))⟧) ∧
(⟦(= λ371 (ite λ152 λ155 λ157))⟧) ∧
(⟦(= λ372 (ite (ite λ367 λ78 false) (store λ370 λ366 λ371) λ370))⟧) ∧
(⟦(= λ373 (ite λ29 (select λ372 λ290) λ263))⟧) ∧
(⟦(= λ374 (ite (= λ311 0) 0 (ite (= λ311 2) λ335 (ite (= λ311 1) λ347 (ite (ite λ348 λ351 false) λ361 (ite λ348 λ363 (ite (= λ311 3) λ365 λ373)))))))⟧) ∧
(⟦(= λ375 (SRC2_OF λ286))⟧) ∧
(⟦(= λ376 (ite λ29 (ite (= λ375 0) 0 (ite (= λ375 λ300) 2 (ite (= λ375 λ306) 1 (ite (= λ375 λ308) 4 (ite (= λ375 λ310) 3 5))))) λ266))⟧) ∧
(⟦(= λ377 (= λ376 4))⟧) ∧
(⟦(= λ378 (ite λ29 (select λ372 λ375) λ268))⟧) ∧
(⟦(= λ379 (ite (= λ376 0) 0 (ite (= λ376 2) λ335 (ite (= λ376 1) λ347 (ite (ite λ377 λ351 false) λ361 (ite λ377 λ363 (ite (= λ376 3) λ365 λ378)))))))⟧) ∧
(⟦(= λ380 (ite (ite λ280 false true) (ite (ite λ283 false true) (ite (= λ288 12) true (ite (= λ288 14) true (ite λ289 true (ite (= λ288 15) (BRANCH_CONDITION λ374 λ379) false)))) false) false))⟧) ∧
(⟦(= λ381 (ite λ27 λ91 λ271))⟧) ∧
(⟦(= λ382 (ite λ281 λ381 λ272))⟧) ∧
(⟦(= λ383 (ite λ289 λ374 (plus (OFFSET_OF λ286) (plus 4 λ382))))⟧) ∧
(⟦(= λ384 (ite λ76 (ite λ53 λ276 (ite λ270 (plus 4 (plus 4 λ273)) (plus 4 (plus 4 λ275)))) λ275))⟧) ∧
(⟦(= λ385 (ite λ380 λ383 λ384))⟧) ∧
(⟦(= λ386 (ite λ74 (ite λ54 λ277 λ385) λ277))⟧) ∧
(⟦(= λ387 (ite λ76 false true))⟧) ∧
(⟦(= λ388 (ite λ387 λ279 (ite λ182 λ279 λ270)))⟧) ∧
(⟦(= λ389 (ite λ30 λ388 λ280))⟧) ∧
(⟦(= λ390 (ite λ75 λ30 false))⟧) ∧
(⟦(= λ391 (ite λ390 λ53 λ282))⟧) ∧
(⟦(= λ392 (ite λ30 λ391 λ283))⟧) ∧
(⟦(= λ393 (ite λ53 true λ387))⟧) ∧
(⟦(= λ394 (ite λ28 (select IMEM_INIT λ116) λ285))⟧) ∧
(⟦(= λ395 (ite λ393 λ286 λ394))⟧) ∧
(⟦(= λ396 (OPCODE_OF λ395))⟧) ∧
(⟦(= λ397 (ite λ30 λ396 λ288))⟧) ∧
(⟦(= λ398 (= λ397 13))⟧) ∧
(⟦(= λ399 (SRC1_OF λ395))⟧) ∧
(⟦(= λ400 (ite CLOCK_INIT true BBUBBLE_S1R_INIT))⟧) ∧
(⟦(= λ401 (ite λ180 λ400 λ291))⟧) ∧
(⟦(= λ402 (ite λ28 λ401 λ292))⟧) ∧
(⟦(= λ403 (ite CLOCK_INIT λ16 BINST_S1R_INIT))⟧) ∧
(⟦(= λ404 (ite λ183 λ293 λ403))⟧) ∧
(⟦(= λ405 (OPCODE_OF λ404))⟧) ∧
(⟦(= λ406 (= λ405 16))⟧) ∧
(⟦(= λ407 (= λ405 10))⟧) ∧
(⟦(= λ408 (= λ405 17))⟧) ∧
(⟦(= λ409 (ite λ28 (ite λ401 0 (ite (ite (ite λ406 false (ite λ407 true λ408)) true λ406) (DEST_OF λ404) 0)) λ298))⟧) ∧
(⟦(= λ410 (ite λ387 λ300 (ite λ402 0 λ409)))⟧) ∧
(⟦(= λ411 (ite CLOCK_INIT true ABUBBLE_S1R_INIT))⟧) ∧
(⟦(= λ412 (ite λ180 λ411 λ301))⟧) ∧
(⟦(= λ413 (= 16 λ186))⟧) ∧
(⟦(= λ414 (= 17 λ186))⟧) ∧
(⟦(= λ415 (= λ186 14))⟧) ∧
(⟦(= λ416 (ite λ28 (ite λ412 0 (ite (ite λ413 false (ite λ414 false (ite λ415 (ite λ178 false true) false))) 31 (ite (ite (ite λ413 false λ414) true λ413) (DEST_OF λ185) 0))) λ305))⟧) ∧
(⟦(= λ417 (ite λ387 λ306 λ416))⟧) ∧
(⟦(= λ418 (ite λ28 λ195 λ307))⟧) ∧
(⟦(= λ419 (ite λ387 λ308 λ418))⟧) ∧
(⟦(= λ420 (ite λ28 λ200 λ309))⟧) ∧
(⟦(= λ421 (ite λ387 λ310 λ420))⟧) ∧
(⟦(= λ422 (ite λ30 (ite (= λ399 0) 0 (ite (= λ410 λ399) 2 (ite (= λ417 λ399) 1 (ite (= λ419 λ399) 4 (ite (= λ421 λ399) 3 5))))) λ311))⟧) ∧
(⟦(= λ423 (ite λ401 false true))⟧) ∧
(⟦(= λ424 (ite λ28 (ite λ407 λ423 false) λ313))⟧) ∧
(⟦(= λ425 (ite λ387 λ314 λ424))⟧) ∧
(⟦(= λ426 (= λ405 11))⟧) ∧
(⟦(= λ427 (ite λ28 (ite λ426 λ423 false) λ316))⟧) ∧
(⟦(= λ428 (ite λ387 λ317 λ427))⟧) ∧
(⟦(= λ429 (SRC1_OF λ404))⟧) ∧
(⟦(= λ430 (ite λ28 (ite (= λ429 0) 0 (ite (= λ429 λ195) 2 (ite (= λ429 λ200) 1 (ite (= λ429 λ202) 4 (ite (= λ429 λ204) 3 5))))) λ319))⟧) ∧
(⟦(= λ431 (= λ430 4))⟧) ∧
(⟦(= λ432 (ite λ28 (select λ262 λ429) λ321))⟧) ∧
(⟦(= λ433 (ite λ387 λ323 (ite (= λ430 0) 0 (ite (= λ430 2) λ226 (ite (= λ430 1) λ237 (ite (ite λ431 λ241 false) λ250 (ite λ431 λ252 (ite (= λ430 3) λ254 λ432))))))))⟧) ∧
(⟦(= λ434 (ite λ28 (SHORT_IMMED_OF λ404) λ324))⟧) ∧
(⟦(= λ435 (SRC2_OF λ404))⟧) ∧
(⟦(= λ436 (ite λ28 (ite (= λ435 0) 0 (ite (= λ435 λ195) 2 (ite (= λ435 λ200) 1 (ite (= λ435 λ202) 4 (ite (= λ435 λ204) 3 5))))) λ326))⟧) ∧
(⟦(= λ437 (= λ436 4))⟧) ∧
(⟦(= λ438 (ite λ28 (select λ262 λ435) λ328))⟧) ∧
(⟦(= λ439 (ite (= λ436 0) 0 (ite (= λ436 2) λ226 (ite (= λ436 1) λ237 (ite (ite λ437 λ241 false) λ250 (ite λ437 λ252 (ite (= λ436 3) λ254 λ438)))))))⟧) ∧
(⟦(= λ440 (ite λ387 λ331 (ite (ite λ28 (ite λ408 true (ite λ407 true λ426)) NO_VALUE6) λ434 λ439)))⟧) ∧
(⟦(= λ441 (ite λ28 λ405 λ332))⟧) ∧
(⟦(= λ442 (ite λ387 λ333 λ441))⟧) ∧
(⟦(= λ443 (ite (ite λ425 true λ428) (plus λ433 λ440) (ALU (ALU_OP_OF λ442) λ433 λ440)))⟧) ∧
(⟦(= λ444 (ite λ30 λ443 λ335))⟧) ∧
(⟦(= λ445 (ite λ28 λ415 λ336))⟧) ∧
(⟦(= λ446 (ite λ387 λ337 λ445))⟧) ∧
(⟦(= λ447 (plus 4 λ116))⟧) ∧
(⟦(= λ448 (ite λ28 (plus 4 λ447) λ339))⟧) ∧
(⟦(= λ449 (ite λ390 λ448 λ340))⟧) ∧
(⟦(= λ450 (ite λ387 λ341 λ187))⟧) ∧
(⟦(= λ451 (ite λ387 λ342 λ264))⟧) ∧
(⟦(= λ452 (ite λ28 λ414 λ343))⟧) ∧
(⟦(= λ453 (ite λ28 (SHORT_IMMED_OF λ185) λ344))⟧) ∧
(⟦(= λ454 (ite λ387 λ346 (ite λ452 λ453 λ269)))⟧) ∧
(⟦(= λ455 (ite λ30 (ite λ446 λ449 (ALU (ALU_OP_OF λ450) λ451 λ454)) λ347))⟧) ∧
(⟦(= λ456 (= λ422 4))⟧) ∧
(⟦(= λ457 (ite λ28 λ207 λ349))⟧) ∧
(⟦(= λ458 (ite λ76 λ457 λ350))⟧) ∧
(⟦(= λ459 (ite λ30 λ458 λ351))⟧) ∧
(⟦(= λ460 (ite λ28 λ210 λ352))⟧) ∧
(⟦(= λ461 (ite λ28 λ225 λ353))⟧) ∧
(⟦(= λ462 (ite λ176 λ354 λ220))⟧) ∧
(⟦(= λ463 (ite λ28 λ462 λ355))⟧) ∧
(⟦(= λ464 (ite (ite λ30 (ite λ460 λ75 false) false) (store λ356 λ461 λ463) λ356))⟧) ∧
(⟦(= λ465 (ite λ28 λ225 λ357))⟧) ∧
(⟦(= λ466 (ite λ80 λ247 λ358))⟧) ∧
(⟦(= λ467 (ite λ28 λ466 λ359))⟧) ∧
(⟦(= λ468 (ite λ30 (select λ464 (ite (ite λ457 λ75 false) λ465 λ467)) λ360))⟧) ∧
(⟦(= λ469 (ite (ite λ458 λ30 false) (ite λ458 λ468 NO_VALUE7) λ361))⟧) ∧
(⟦(= λ470 (ite λ387 λ362 λ226))⟧) ∧
(⟦(= λ471 (ite λ30 λ470 λ363))⟧) ∧
(⟦(= λ472 (ite λ387 λ364 λ237))⟧) ∧
(⟦(= λ473 (ite λ30 λ472 λ365))⟧) ∧
(⟦(= λ474 (ite λ28 λ202 λ366))⟧) ∧
(⟦(= λ475 (ite λ28 λ204 λ368))⟧) ∧
(⟦(= λ476 (ite (ite (ite (= λ475 0) false true) λ76 false) (store λ372 λ475 λ254) λ372))⟧) ∧
(⟦(= λ477 (ite (ite (ite (= λ474 0) false true) λ76 false) (store λ476 λ474 (ite λ241 λ250 λ252)) λ476))⟧) ∧
(⟦(= λ478 (ite λ30 (select λ477 λ399) λ373))⟧) ∧
(⟦(= λ479 (ite (= λ422 0) 0 (ite (= λ422 2) λ444 (ite (= λ422 1) λ455 (ite (ite λ456 λ459 false) λ469 (ite λ456 λ471 (ite (= λ422 3) λ473 λ478)))))))⟧) ∧
(⟦(= λ480 (SRC2_OF λ395))⟧) ∧
(⟦(= λ481 (ite λ30 (ite (= λ480 0) 0 (ite (= λ480 λ410) 2 (ite (= λ480 λ417) 1 (ite (= λ480 λ419) 4 (ite (= λ480 λ421) 3 5))))) λ376))⟧) ∧
(⟦(= λ482 (= λ481 4))⟧) ∧
(⟦(= λ483 (ite λ30 (select λ477 λ480) λ378))⟧) ∧
(⟦(= λ484 (ite (= λ481 0) 0 (ite (= λ481 2) λ444 (ite (= λ481 1) λ455 (ite (ite λ482 λ459 false) λ469 (ite λ482 λ471 (ite (= λ481 3) λ473 λ483)))))))⟧) ∧
(⟦(= λ485 (ite (ite λ389 false true) (ite (ite λ392 false true) (ite (= λ397 12) true (ite (= λ397 14) true (ite λ398 true (ite (= λ397 15) (BRANCH_CONDITION λ479 λ484) false)))) false) false))⟧) ∧
(⟦(= λ486 (ite λ28 λ116 λ381))⟧) ∧
(⟦(= λ487 (ite λ390 λ486 λ382))⟧) ∧
(⟦(= λ488 (ite λ398 λ479 (plus (OFFSET_OF λ395) (plus 4 λ487))))⟧) ∧
(⟦(= λ489 (ite λ74 (ite λ54 λ385 (ite λ380 (plus 4 (plus 4 λ383)) (plus 4 (plus 4 λ384)))) λ384))⟧) ∧
(⟦(= λ490 (ite λ485 λ488 λ489))⟧) ∧
(⟦(= λ491 (ite λ72 (ite λ55 λ386 λ490) λ386))⟧) ∧
(⟦(= λ492 (ite λ74 false true))⟧) ∧
(⟦(= λ493 (ite λ492 λ388 (ite λ283 λ388 λ380)))⟧) ∧
(⟦(= λ494 (ite λ31 λ493 λ389))⟧) ∧
(⟦(= λ495 (ite λ73 λ31 false))⟧) ∧
(⟦(= λ496 (ite λ495 λ54 λ391))⟧) ∧
(⟦(= λ497 (ite λ31 λ496 λ392))⟧) ∧
(⟦(= λ498 (ite λ54 true λ492))⟧) ∧
(⟦(= λ499 (ite λ29 (select IMEM_INIT λ175) λ394))⟧) ∧
(⟦(= λ500 (ite λ498 λ395 λ499))⟧) ∧
(⟦(= λ501 (OPCODE_OF λ500))⟧) ∧
(⟦(= λ502 (ite λ31 λ501 λ397))⟧) ∧
(⟦(= λ503 (= λ502 13))⟧) ∧
(⟦(= λ504 (SRC1_OF λ500))⟧) ∧
(⟦(= λ505 (ite λ27 true λ400))⟧) ∧
(⟦(= λ506 (ite λ281 λ505 λ401))⟧) ∧
(⟦(= λ507 (ite λ29 λ506 λ402))⟧) ∧
(⟦(= λ508 (ite λ27 (select IMEM_INIT λ338) λ403))⟧) ∧
(⟦(= λ509 (ite λ284 λ404 λ508))⟧) ∧
(⟦(= λ510 (OPCODE_OF λ509))⟧) ∧
(⟦(= λ511 (= λ510 16))⟧) ∧
(⟦(= λ512 (= λ510 10))⟧) ∧
(⟦(= λ513 (= λ510 17))⟧) ∧
(⟦(= λ514 (ite λ29 (ite λ506 0 (ite (ite (ite λ511 false (ite λ512 true λ513)) true λ511) (DEST_OF λ509) 0)) λ409))⟧) ∧
(⟦(= λ515 (ite λ492 λ410 (ite λ507 0 λ514)))⟧) ∧
(⟦(= λ516 (ite λ27 true λ411))⟧) ∧
(⟦(= λ517 (ite λ281 λ516 λ412))⟧) ∧
(⟦(= λ518 (= λ287 16))⟧) ∧
(⟦(= λ519 (= λ287 17))⟧) ∧
(⟦(= λ520 (= λ287 14))⟧) ∧
(⟦(= λ521 (ite λ29 (ite λ517 0 (ite (ite λ518 false (ite λ519 false (ite λ520 (ite λ279 false true) false))) 31 (ite (ite (ite λ518 false λ519) true λ518) (DEST_OF λ286) 0))) λ416))⟧) ∧
(⟦(= λ522 (ite λ492 λ417 λ521))⟧) ∧
(⟦(= λ523 (ite λ29 λ300 λ418))⟧) ∧
(⟦(= λ524 (ite λ492 λ419 λ523))⟧) ∧
(⟦(= λ525 (ite λ29 λ306 λ420))⟧) ∧
(⟦(= λ526 (ite λ492 λ421 λ525))⟧) ∧
(⟦(= λ527 (ite λ31 (ite (= λ504 0) 0 (ite (= λ515 λ504) 2 (ite (= λ522 λ504) 1 (ite (= λ524 λ504) 4 (ite (= λ526 λ504) 3 5))))) λ422))⟧) ∧
(⟦(= λ528 (ite λ506 false true))⟧) ∧
(⟦(= λ529 (ite λ29 (ite λ512 λ528 false) λ424))⟧) ∧
(⟦(= λ530 (ite λ492 λ425 λ529))⟧) ∧
(⟦(= λ531 (= λ510 11))⟧) ∧
(⟦(= λ532 (ite λ29 (ite λ531 λ528 false) λ427))⟧) ∧
(⟦(= λ533 (ite λ492 λ428 λ532))⟧) ∧
(⟦(= λ534 (SRC1_OF λ509))⟧) ∧
(⟦(= λ535 (ite λ29 (ite (= λ534 0) 0 (ite (= λ534 λ300) 2 (ite (= λ534 λ306) 1 (ite (= λ534 λ308) 4 (ite (= λ534 λ310) 3 5))))) λ430))⟧) ∧
(⟦(= λ536 (= λ535 4))⟧) ∧
(⟦(= λ537 (ite λ29 (select λ372 λ534) λ432))⟧) ∧
(⟦(= λ538 (ite λ492 λ433 (ite (= λ535 0) 0 (ite (= λ535 2) λ335 (ite (= λ535 1) λ347 (ite (ite λ536 λ351 false) λ361 (ite λ536 λ363 (ite (= λ535 3) λ365 λ537))))))))⟧) ∧
(⟦(= λ539 (ite λ29 (SHORT_IMMED_OF λ509) λ434))⟧) ∧
(⟦(= λ540 (SRC2_OF λ509))⟧) ∧
(⟦(= λ541 (ite λ29 (ite (= λ540 0) 0 (ite (= λ540 λ300) 2 (ite (= λ540 λ306) 1 (ite (= λ540 λ308) 4 (ite (= λ540 λ310) 3 5))))) λ436))⟧) ∧
(⟦(= λ542 (= λ541 4))⟧) ∧
(⟦(= λ543 (ite λ29 (select λ372 λ540) λ438))⟧) ∧
(⟦(= λ544 (ite (= λ541 0) 0 (ite (= λ541 2) λ335 (ite (= λ541 1) λ347 (ite (ite λ542 λ351 false) λ361 (ite λ542 λ363 (ite (= λ541 3) λ365 λ543)))))))⟧) ∧
(⟦(= λ545 (ite λ492 λ440 (ite (ite λ29 (ite λ513 true (ite λ512 true λ531)) NO_VALUE8) λ539 λ544)))⟧) ∧
(⟦(= λ546 (ite λ29 λ510 λ441))⟧) ∧
(⟦(= λ547 (ite λ492 λ442 λ546))⟧) ∧
(⟦(= λ548 (ite (ite λ530 true λ533) (plus λ538 λ545) (ALU (ALU_OP_OF λ547) λ538 λ545)))⟧) ∧
(⟦(= λ549 (ite λ31 λ548 λ444))⟧) ∧
(⟦(= λ550 (ite λ29 λ520 λ445))⟧) ∧
(⟦(= λ551 (ite λ492 λ446 λ550))⟧) ∧
(⟦(= λ552 (plus 4 λ175))⟧) ∧
(⟦(= λ553 (ite λ29 (plus 4 λ552) λ448))⟧) ∧
(⟦(= λ554 (ite λ495 λ553 λ449))⟧) ∧
(⟦(= λ555 (ite λ492 λ450 λ288))⟧) ∧
(⟦(= λ556 (ite λ492 λ451 λ374))⟧) ∧
(⟦(= λ557 (ite λ29 λ519 λ452))⟧) ∧
(⟦(= λ558 (ite λ29 (SHORT_IMMED_OF λ286) λ453))⟧) ∧
(⟦(= λ559 (ite λ492 λ454 (ite λ557 λ558 λ379)))⟧) ∧
(⟦(= λ560 (ite λ31 (ite λ551 λ554 (ALU (ALU_OP_OF λ555) λ556 λ559)) λ455))⟧) ∧
(⟦(= λ561 (= λ527 4))⟧) ∧
(⟦(= λ562 (ite λ29 λ314 λ457))⟧) ∧
(⟦(= λ563 (ite λ74 λ562 λ458))⟧) ∧
(⟦(= λ564 (ite λ31 λ563 λ459))⟧) ∧
(⟦(= λ565 (ite λ29 λ317 λ460))⟧) ∧
(⟦(= λ566 (ite λ29 λ334 λ461))⟧) ∧
(⟦(= λ567 (ite λ278 λ462 λ329))⟧) ∧
(⟦(= λ568 (ite λ29 λ567 λ463))⟧) ∧
(⟦(= λ569 (ite (ite λ31 (ite λ565 λ73 false) false) (store λ464 λ566 λ568) λ464))⟧) ∧
(⟦(= λ570 (ite λ29 λ334 λ465))⟧) ∧
(⟦(= λ571 (ite λ78 λ357 λ466))⟧) ∧
(⟦(= λ572 (ite λ29 λ571 λ467))⟧) ∧
(⟦(= λ573 (ite λ31 (select λ569 (ite (ite λ562 λ73 false) λ570 λ572)) λ468))⟧) ∧
(⟦(= λ574 (ite (ite λ563 λ31 false) (ite λ563 λ573 NO_VALUE9) λ469))⟧) ∧
(⟦(= λ575 (ite λ492 λ470 λ335))⟧) ∧
(⟦(= λ576 (ite λ31 λ575 λ471))⟧) ∧
(⟦(= λ577 (ite λ492 λ472 λ347))⟧) ∧
(⟦(= λ578 (ite λ31 λ577 λ473))⟧) ∧
(⟦(= λ579 (ite λ29 λ308 λ474))⟧) ∧
(⟦(= λ580 (ite λ29 λ310 λ475))⟧) ∧
(⟦(= λ581 (ite (ite (ite (= λ580 0) false true) λ74 false) (store λ477 λ580 λ365) λ477))⟧) ∧
(⟦(= λ582 (ite (ite (ite (= λ579 0) false true) λ74 false) (store λ581 λ579 (ite λ351 λ361 λ363)) λ581))⟧) ∧
(⟦(= λ583 (ite λ31 (select λ582 λ504) λ478))⟧) ∧
(⟦(= λ584 (ite (= λ527 0) 0 (ite (= λ527 2) λ549 (ite (= λ527 1) λ560 (ite (ite λ561 λ564 false) λ574 (ite λ561 λ576 (ite (= λ527 3) λ578 λ583)))))))⟧) ∧
(⟦(= λ585 (SRC2_OF λ500))⟧) ∧
(⟦(= λ586 (ite λ31 (ite (= λ585 0) 0 (ite (= λ585 λ515) 2 (ite (= λ585 λ522) 1 (ite (= λ585 λ524) 4 (ite (= λ585 λ526) 3 5))))) λ481))⟧) ∧
(⟦(= λ587 (= λ586 4))⟧) ∧
(⟦(= λ588 (ite λ31 (select λ582 λ585) λ483))⟧) ∧
(⟦(= λ589 (ite (= λ586 0) 0 (ite (= λ586 2) λ549 (ite (= λ586 1) λ560 (ite (ite λ587 λ564 false) λ574 (ite λ587 λ576 (ite (= λ586 3) λ578 λ588)))))))⟧) ∧
(⟦(= λ590 (ite (ite λ494 false true) (ite (ite λ497 false true) (ite (= λ502 12) true (ite (= λ502 14) true (ite λ503 true (ite (= λ502 15) (BRANCH_CONDITION λ584 λ589) false)))) false) false))⟧) ∧
(⟦(= λ591 (ite λ29 λ175 λ486))⟧) ∧
(⟦(= λ592 (ite λ495 λ591 λ487))⟧) ∧
(⟦(= λ593 (ite λ503 λ584 (plus (OFFSET_OF λ500) (plus 4 λ592))))⟧) ∧
(⟦(= λ594 (ite λ72 (ite λ55 λ490 (ite λ485 (plus 4 (plus 4 λ488)) (plus 4 (plus 4 λ489)))) λ489))⟧) ∧
(⟦(= λ595 (ite λ590 λ593 λ594))⟧) ∧
(⟦(= λ596 (ite λ70 (ite λ56 λ491 λ595) λ491))⟧) ∧
(⟦(= λ597 (ite λ72 false true))⟧) ∧
(⟦(= λ598 (ite λ597 λ493 (ite λ392 λ493 λ485)))⟧) ∧
(⟦(= λ599 (ite λ32 λ598 λ494))⟧) ∧
(⟦(= λ600 (ite λ71 λ32 false))⟧) ∧
(⟦(= λ601 (ite λ600 λ55 λ496))⟧) ∧
(⟦(= λ602 (ite λ32 λ601 λ497))⟧) ∧
(⟦(= λ603 (ite λ55 true λ597))⟧) ∧
(⟦(= λ604 (ite λ30 (select IMEM_INIT λ277) λ499))⟧) ∧
(⟦(= λ605 (ite λ603 λ500 λ604))⟧) ∧
(⟦(= λ606 (OPCODE_OF λ605))⟧) ∧
(⟦(= λ607 (ite λ32 λ606 λ502))⟧) ∧
(⟦(= λ608 (= λ607 13))⟧) ∧
(⟦(= λ609 (SRC1_OF λ605))⟧) ∧
(⟦(= λ610 (ite λ28 true λ505))⟧) ∧
(⟦(= λ611 (ite λ390 λ610 λ506))⟧) ∧
(⟦(= λ612 (ite λ30 λ611 λ507))⟧) ∧
(⟦(= λ613 (ite λ28 (select IMEM_INIT λ447) λ508))⟧) ∧
(⟦(= λ614 (ite λ393 λ509 λ613))⟧) ∧
(⟦(= λ615 (OPCODE_OF λ614))⟧) ∧
(⟦(= λ616 (= λ615 16))⟧) ∧
(⟦(= λ617 (= λ615 10))⟧) ∧
(⟦(= λ618 (= λ615 17))⟧) ∧
(⟦(= λ619 (ite λ30 (ite λ611 0 (ite (ite (ite λ616 false (ite λ617 true λ618)) true λ616) (DEST_OF λ614) 0)) λ514))⟧) ∧
(⟦(= λ620 (ite λ597 λ515 (ite λ612 0 λ619)))⟧) ∧
(⟦(= λ621 (ite λ28 true λ516))⟧) ∧
(⟦(= λ622 (ite λ390 λ621 λ517))⟧) ∧
(⟦(= λ623 (= λ396 16))⟧) ∧
(⟦(= λ624 (= λ396 17))⟧) ∧
(⟦(= λ625 (= λ396 14))⟧) ∧
(⟦(= λ626 (ite λ30 (ite λ622 0 (ite (ite λ623 false (ite λ624 false (ite λ625 (ite λ388 false true) false))) 31 (ite (ite (ite λ623 false λ624) true λ623) (DEST_OF λ395) 0))) λ521))⟧) ∧
(⟦(= λ627 (ite λ597 λ522 λ626))⟧) ∧
(⟦(= λ628 (ite λ30 λ410 λ523))⟧) ∧
(⟦(= λ629 (ite λ597 λ524 λ628))⟧) ∧
(⟦(= λ630 (ite λ30 λ417 λ525))⟧) ∧
(⟦(= λ631 (ite λ597 λ526 λ630))⟧) ∧
(⟦(= λ632 (ite λ32 (ite (= λ609 0) 0 (ite (= λ620 λ609) 2 (ite (= λ627 λ609) 1 (ite (= λ629 λ609) 4 (ite (= λ631 λ609) 3 5))))) λ527))⟧) ∧
(⟦(= λ633 (ite λ611 false true))⟧) ∧
(⟦(= λ634 (ite λ30 (ite λ617 λ633 false) λ529))⟧) ∧
(⟦(= λ635 (ite λ597 λ530 λ634))⟧) ∧
(⟦(= λ636 (= λ615 11))⟧) ∧
(⟦(= λ637 (ite λ30 (ite λ636 λ633 false) λ532))⟧) ∧
(⟦(= λ638 (ite λ597 λ533 λ637))⟧) ∧
(⟦(= λ639 (SRC1_OF λ614))⟧) ∧
(⟦(= λ640 (ite λ30 (ite (= λ639 0) 0 (ite (= λ639 λ410) 2 (ite (= λ639 λ417) 1 (ite (= λ639 λ419) 4 (ite (= λ639 λ421) 3 5))))) λ535))⟧) ∧
(⟦(= λ641 (= λ640 4))⟧) ∧
(⟦(= λ642 (ite λ30 (select λ477 λ639) λ537))⟧) ∧
(⟦(= λ643 (ite λ597 λ538 (ite (= λ640 0) 0 (ite (= λ640 2) λ444 (ite (= λ640 1) λ455 (ite (ite λ641 λ459 false) λ469 (ite λ641 λ471 (ite (= λ640 3) λ473 λ642))))))))⟧) ∧
(⟦(= λ644 (ite λ30 (SHORT_IMMED_OF λ614) λ539))⟧) ∧
(⟦(= λ645 (SRC2_OF λ614))⟧) ∧
(⟦(= λ646 (ite λ30 (ite (= λ645 0) 0 (ite (= λ645 λ410) 2 (ite (= λ645 λ417) 1 (ite (= λ645 λ419) 4 (ite (= λ645 λ421) 3 5))))) λ541))⟧) ∧
(⟦(= λ647 (= λ646 4))⟧) ∧
(⟦(= λ648 (ite λ30 (select λ477 λ645) λ543))⟧) ∧
(⟦(= λ649 (ite (= λ646 0) 0 (ite (= λ646 2) λ444 (ite (= λ646 1) λ455 (ite (ite λ647 λ459 false) λ469 (ite λ647 λ471 (ite (= λ646 3) λ473 λ648)))))))⟧) ∧
(⟦(= λ650 (ite λ597 λ545 (ite (ite λ30 (ite λ618 true (ite λ617 true λ636)) NO_VALUE10) λ644 λ649)))⟧) ∧
(⟦(= λ651 (ite λ30 λ615 λ546))⟧) ∧
(⟦(= λ652 (ite λ597 λ547 λ651))⟧) ∧
(⟦(= λ653 (ite (ite λ635 true λ638) (plus λ643 λ650) (ALU (ALU_OP_OF λ652) λ643 λ650)))⟧) ∧
(⟦(= λ654 (ite λ32 λ653 λ549))⟧) ∧
(⟦(= λ655 (ite λ30 λ625 λ550))⟧) ∧
(⟦(= λ656 (ite λ597 λ551 λ655))⟧) ∧
(⟦(= λ657 (plus 4 λ277))⟧) ∧
(⟦(= λ658 (ite λ30 (plus 4 λ657) λ553))⟧) ∧
(⟦(= λ659 (ite λ600 λ658 λ554))⟧) ∧
(⟦(= λ660 (ite λ597 λ555 λ397))⟧) ∧
(⟦(= λ661 (ite λ597 λ556 λ479))⟧) ∧
(⟦(= λ662 (ite λ30 λ624 λ557))⟧) ∧
(⟦(= λ663 (ite λ30 (SHORT_IMMED_OF λ395) λ558))⟧) ∧
(⟦(= λ664 (ite λ597 λ559 (ite λ662 λ663 λ484)))⟧) ∧
(⟦(= λ665 (ite λ32 (ite λ656 λ659 (ALU (ALU_OP_OF λ660) λ661 λ664)) λ560))⟧) ∧
(⟦(= λ666 (= λ632 4))⟧) ∧
(⟦(= λ667 (ite λ30 λ425 λ562))⟧) ∧
(⟦(= λ668 (ite λ72 λ667 λ563))⟧) ∧
(⟦(= λ669 (ite λ32 λ668 λ564))⟧) ∧
(⟦(= λ670 (ite λ30 λ428 λ565))⟧) ∧
(⟦(= λ671 (ite λ30 λ443 λ566))⟧) ∧
(⟦(= λ672 (ite λ387 λ567 λ439))⟧) ∧
(⟦(= λ673 (ite λ30 λ672 λ568))⟧) ∧
(⟦(= λ674 (ite (ite λ32 (ite λ670 λ71 false) false) (store λ569 λ671 λ673) λ569))⟧) ∧
(⟦(= λ675 (ite λ30 λ443 λ570))⟧) ∧
(⟦(= λ676 (ite λ76 λ465 λ571))⟧) ∧
(⟦(= λ677 (ite λ30 λ676 λ572))⟧) ∧
(⟦(= λ678 (ite λ32 (select λ674 (ite (ite λ667 λ71 false) λ675 λ677)) λ573))⟧) ∧
(⟦(= λ679 (ite (ite λ668 λ32 false) (ite λ668 λ678 NO_VALUE11) λ574))⟧) ∧
(⟦(= λ680 (ite λ597 λ575 λ444))⟧) ∧
(⟦(= λ681 (ite λ32 λ680 λ576))⟧) ∧
(⟦(= λ682 (ite λ597 λ577 λ455))⟧) ∧
(⟦(= λ683 (ite λ32 λ682 λ578))⟧) ∧
(⟦(= λ684 (ite λ30 λ419 λ579))⟧) ∧
(⟦(= λ685 (ite λ30 λ421 λ580))⟧) ∧
(⟦(= λ686 (ite (ite (ite (= λ685 0) false true) λ72 false) (store λ582 λ685 λ473) λ582))⟧) ∧
(⟦(= λ687 (ite (ite (ite (= λ684 0) false true) λ72 false) (store λ686 λ684 (ite λ459 λ469 λ471)) λ686))⟧) ∧
(⟦(= λ688 (ite λ32 (select λ687 λ609) λ583))⟧) ∧
(⟦(= λ689 (ite (= λ632 0) 0 (ite (= λ632 2) λ654 (ite (= λ632 1) λ665 (ite (ite λ666 λ669 false) λ679 (ite λ666 λ681 (ite (= λ632 3) λ683 λ688)))))))⟧) ∧
(⟦(= λ690 (SRC2_OF λ605))⟧) ∧
(⟦(= λ691 (ite λ32 (ite (= λ690 0) 0 (ite (= λ690 λ620) 2 (ite (= λ690 λ627) 1 (ite (= λ690 λ629) 4 (ite (= λ690 λ631) 3 5))))) λ586))⟧) ∧
(⟦(= λ692 (= λ691 4))⟧) ∧
(⟦(= λ693 (ite λ32 (select λ687 λ690) λ588))⟧) ∧
(⟦(= λ694 (ite (= λ691 0) 0 (ite (= λ691 2) λ654 (ite (= λ691 1) λ665 (ite (ite λ692 λ669 false) λ679 (ite λ692 λ681 (ite (= λ691 3) λ683 λ693)))))))⟧) ∧
(⟦(= λ695 (ite (ite λ599 false true) (ite (ite λ602 false true) (ite (= λ607 12) true (ite (= λ607 14) true (ite λ608 true (ite (= λ607 15) (BRANCH_CONDITION λ689 λ694) false)))) false) false))⟧) ∧
(⟦(= λ696 (ite λ30 λ277 λ591))⟧) ∧
(⟦(= λ697 (ite λ600 λ696 λ592))⟧) ∧
(⟦(= λ698 (ite λ608 λ689 (plus (OFFSET_OF λ605) (plus 4 λ697))))⟧) ∧
(⟦(= λ699 (ite λ70 (ite λ56 λ595 (ite λ590 (plus 4 (plus 4 λ593)) (plus 4 (plus 4 λ594)))) λ594))⟧) ∧
(⟦(= λ700 (ite λ695 λ698 λ699))⟧) ∧
(⟦(= λ701 (ite λ68 (ite λ57 λ596 λ700) λ596))⟧) ∧
(⟦(= λ702 (ite λ70 false true))⟧) ∧
(⟦(= λ703 (ite λ702 λ598 (ite λ497 λ598 λ590)))⟧) ∧
(⟦(= λ704 (ite λ33 λ703 λ599))⟧) ∧
(⟦(= λ705 (ite λ69 λ33 false))⟧) ∧
(⟦(= λ706 (ite λ705 λ56 λ601))⟧) ∧
(⟦(= λ707 (ite λ33 λ706 λ602))⟧) ∧
(⟦(= λ708 (ite λ56 true λ702))⟧) ∧
(⟦(= λ709 (ite λ31 (select IMEM_INIT λ386) λ604))⟧) ∧
(⟦(= λ710 (ite λ708 λ605 λ709))⟧) ∧
(⟦(= λ711 (OPCODE_OF λ710))⟧) ∧
(⟦(= λ712 (ite λ33 λ711 λ607))⟧) ∧
(⟦(= λ713 (= λ712 13))⟧) ∧
(⟦(= λ714 (SRC1_OF λ710))⟧) ∧
(⟦(= λ715 (ite λ29 true λ610))⟧) ∧
(⟦(= λ716 (ite λ495 λ715 λ611))⟧) ∧
(⟦(= λ717 (ite λ31 λ716 λ612))⟧) ∧
(⟦(= λ718 (ite λ29 (select IMEM_INIT λ552) λ613))⟧) ∧
(⟦(= λ719 (ite λ498 λ614 λ718))⟧) ∧
(⟦(= λ720 (OPCODE_OF λ719))⟧) ∧
(⟦(= λ721 (= λ720 16))⟧) ∧
(⟦(= λ722 (= λ720 10))⟧) ∧
(⟦(= λ723 (= λ720 17))⟧) ∧
(⟦(= λ724 (ite λ31 (ite λ716 0 (ite (ite (ite λ721 false (ite λ722 true λ723)) true λ721) (DEST_OF λ719) 0)) λ619))⟧) ∧
(⟦(= λ725 (ite λ702 λ620 (ite λ717 0 λ724)))⟧) ∧
(⟦(= λ726 (ite λ29 true λ621))⟧) ∧
(⟦(= λ727 (ite λ495 λ726 λ622))⟧) ∧
(⟦(= λ728 (= λ501 16))⟧) ∧
(⟦(= λ729 (= λ501 17))⟧) ∧
(⟦(= λ730 (= λ501 14))⟧) ∧
(⟦(= λ731 (ite λ31 (ite λ727 0 (ite (ite λ728 false (ite λ729 false (ite λ730 (ite λ493 false true) false))) 31 (ite (ite (ite λ728 false λ729) true λ728) (DEST_OF λ500) 0))) λ626))⟧) ∧
(⟦(= λ732 (ite λ702 λ627 λ731))⟧) ∧
(⟦(= λ733 (ite λ31 λ515 λ628))⟧) ∧
(⟦(= λ734 (ite λ702 λ629 λ733))⟧) ∧
(⟦(= λ735 (ite λ31 λ522 λ630))⟧) ∧
(⟦(= λ736 (ite λ702 λ631 λ735))⟧) ∧
(⟦(= λ737 (ite λ33 (ite (= λ714 0) 0 (ite (= λ725 λ714) 2 (ite (= λ732 λ714) 1 (ite (= λ734 λ714) 4 (ite (= λ736 λ714) 3 5))))) λ632))⟧) ∧
(⟦(= λ738 (ite λ716 false true))⟧) ∧
(⟦(= λ739 (ite λ31 (ite λ722 λ738 false) λ634))⟧) ∧
(⟦(= λ740 (ite λ702 λ635 λ739))⟧) ∧
(⟦(= λ741 (= λ720 11))⟧) ∧
(⟦(= λ742 (ite λ31 (ite λ741 λ738 false) λ637))⟧) ∧
(⟦(= λ743 (ite λ702 λ638 λ742))⟧) ∧
(⟦(= λ744 (SRC1_OF λ719))⟧) ∧
(⟦(= λ745 (ite λ31 (ite (= λ744 0) 0 (ite (= λ744 λ515) 2 (ite (= λ744 λ522) 1 (ite (= λ744 λ524) 4 (ite (= λ744 λ526) 3 5))))) λ640))⟧) ∧
(⟦(= λ746 (= λ745 4))⟧) ∧
(⟦(= λ747 (ite λ31 (select λ582 λ744) λ642))⟧) ∧
(⟦(= λ748 (ite λ702 λ643 (ite (= λ745 0) 0 (ite (= λ745 2) λ549 (ite (= λ745 1) λ560 (ite (ite λ746 λ564 false) λ574 (ite λ746 λ576 (ite (= λ745 3) λ578 λ747))))))))⟧) ∧
(⟦(= λ749 (ite λ31 (SHORT_IMMED_OF λ719) λ644))⟧) ∧
(⟦(= λ750 (SRC2_OF λ719))⟧) ∧
(⟦(= λ751 (ite λ31 (ite (= λ750 0) 0 (ite (= λ750 λ515) 2 (ite (= λ750 λ522) 1 (ite (= λ750 λ524) 4 (ite (= λ750 λ526) 3 5))))) λ646))⟧) ∧
(⟦(= λ752 (= λ751 4))⟧) ∧
(⟦(= λ753 (ite λ31 (select λ582 λ750) λ648))⟧) ∧
(⟦(= λ754 (ite (= λ751 0) 0 (ite (= λ751 2) λ549 (ite (= λ751 1) λ560 (ite (ite λ752 λ564 false) λ574 (ite λ752 λ576 (ite (= λ751 3) λ578 λ753)))))))⟧) ∧
(⟦(= λ755 (ite λ702 λ650 (ite (ite λ31 (ite λ723 true (ite λ722 true λ741)) NO_VALUE12) λ749 λ754)))⟧) ∧
(⟦(= λ756 (ite λ31 λ720 λ651))⟧) ∧
(⟦(= λ757 (ite λ702 λ652 λ756))⟧) ∧
(⟦(= λ758 (ite (ite λ740 true λ743) (plus λ748 λ755) (ALU (ALU_OP_OF λ757) λ748 λ755)))⟧) ∧
(⟦(= λ759 (ite λ33 λ758 λ654))⟧) ∧
(⟦(= λ760 (ite λ31 λ730 λ655))⟧) ∧
(⟦(= λ761 (ite λ702 λ656 λ760))⟧) ∧
(⟦(= λ762 (plus 4 λ386))⟧) ∧
(⟦(= λ763 (ite λ31 (plus 4 λ762) λ658))⟧) ∧
(⟦(= λ764 (ite λ705 λ763 λ659))⟧) ∧
(⟦(= λ765 (ite λ702 λ660 λ502))⟧) ∧
(⟦(= λ766 (ite λ702 λ661 λ584))⟧) ∧
(⟦(= λ767 (ite λ31 λ729 λ662))⟧) ∧
(⟦(= λ768 (ite λ31 (SHORT_IMMED_OF λ500) λ663))⟧) ∧
(⟦(= λ769 (ite λ702 λ664 (ite λ767 λ768 λ589)))⟧) ∧
(⟦(= λ770 (ite λ33 (ite λ761 λ764 (ALU (ALU_OP_OF λ765) λ766 λ769)) λ665))⟧) ∧
(⟦(= λ771 (= λ737 4))⟧) ∧
(⟦(= λ772 (ite λ31 λ530 λ667))⟧) ∧
(⟦(= λ773 (ite λ70 λ772 λ668))⟧) ∧
(⟦(= λ774 (ite λ33 λ773 λ669))⟧) ∧
(⟦(= λ775 (ite λ31 λ533 λ670))⟧) ∧
(⟦(= λ776 (ite λ31 λ548 λ671))⟧) ∧
(⟦(= λ777 (ite λ492 λ672 λ544))⟧) ∧
(⟦(= λ778 (ite λ31 λ777 λ673))⟧) ∧
(⟦(= λ779 (ite (ite λ33 (ite λ775 λ69 false) false) (store λ674 λ776 λ778) λ674))⟧) ∧
(⟦(= λ780 (ite λ31 λ548 λ675))⟧) ∧
(⟦(= λ781 (ite λ74 λ570 λ676))⟧) ∧
(⟦(= λ782 (ite λ31 λ781 λ677))⟧) ∧
(⟦(= λ783 (ite λ33 (select λ779 (ite (ite λ772 λ69 false) λ780 λ782)) λ678))⟧) ∧
(⟦(= λ784 (ite (ite λ773 λ33 false) (ite λ773 λ783 NO_VALUE13) λ679))⟧) ∧
(⟦(= λ785 (ite λ702 λ680 λ549))⟧) ∧
(⟦(= λ786 (ite λ33 λ785 λ681))⟧) ∧
(⟦(= λ787 (ite λ702 λ682 λ560))⟧) ∧
(⟦(= λ788 (ite λ33 λ787 λ683))⟧) ∧
(⟦(= λ789 (ite λ31 λ524 λ684))⟧) ∧
(⟦(= λ790 (ite λ31 λ526 λ685))⟧) ∧
(⟦(= λ791 (ite (ite (ite (= λ790 0) false true) λ70 false) (store λ687 λ790 λ578) λ687))⟧) ∧
(⟦(= λ792 (ite (ite (ite (= λ789 0) false true) λ70 false) (store λ791 λ789 (ite λ564 λ574 λ576)) λ791))⟧) ∧
(⟦(= λ793 (ite λ33 (select λ792 λ714) λ688))⟧) ∧
(⟦(= λ794 (ite (= λ737 0) 0 (ite (= λ737 2) λ759 (ite (= λ737 1) λ770 (ite (ite λ771 λ774 false) λ784 (ite λ771 λ786 (ite (= λ737 3) λ788 λ793)))))))⟧) ∧
(⟦(= λ795 (SRC2_OF λ710))⟧) ∧
(⟦(= λ796 (ite λ33 (ite (= λ795 0) 0 (ite (= λ795 λ725) 2 (ite (= λ795 λ732) 1 (ite (= λ795 λ734) 4 (ite (= λ795 λ736) 3 5))))) λ691))⟧) ∧
(⟦(= λ797 (= λ796 4))⟧) ∧
(⟦(= λ798 (ite λ33 (select λ792 λ795) λ693))⟧) ∧
(⟦(= λ799 (ite (= λ796 0) 0 (ite (= λ796 2) λ759 (ite (= λ796 1) λ770 (ite (ite λ797 λ774 false) λ784 (ite λ797 λ786 (ite (= λ796 3) λ788 λ798)))))))⟧) ∧
(⟦(= λ800 (ite (ite λ704 false true) (ite (ite λ707 false true) (ite (= λ712 12) true (ite (= λ712 14) true (ite λ713 true (ite (= λ712 15) (BRANCH_CONDITION λ794 λ799) false)))) false) false))⟧) ∧
(⟦(= λ801 (ite λ31 λ386 λ696))⟧) ∧
(⟦(= λ802 (ite λ705 λ801 λ697))⟧) ∧
(⟦(= λ803 (ite λ713 λ794 (plus (OFFSET_OF λ710) (plus 4 λ802))))⟧) ∧
(⟦(= λ804 (ite λ68 (ite λ57 λ700 (ite λ695 (plus 4 (plus 4 λ698)) (plus 4 (plus 4 λ699)))) λ699))⟧) ∧
(⟦(= λ805 (ite λ800 λ803 λ804))⟧) ∧
(⟦(= λ806 (ite λ66 (ite λ58 λ701 λ805) λ701))⟧) ∧
(⟦(= λ807 (ite λ68 false true))⟧) ∧
(⟦(= λ808 (ite λ807 λ703 (ite λ602 λ703 λ695)))⟧) ∧
(⟦(= λ809 (ite λ34 λ808 λ704))⟧) ∧
(⟦(= λ810 (ite λ67 λ34 false))⟧) ∧
(⟦(= λ811 (ite λ810 λ57 λ706))⟧) ∧
(⟦(= λ812 (ite λ34 λ811 λ707))⟧) ∧
(⟦(= λ813 (ite λ57 true λ807))⟧) ∧
(⟦(= λ814 (ite λ32 (select IMEM_INIT λ491) λ709))⟧) ∧
(⟦(= λ815 (ite λ813 λ710 λ814))⟧) ∧
(⟦(= λ816 (OPCODE_OF λ815))⟧) ∧
(⟦(= λ817 (ite λ34 λ816 λ712))⟧) ∧
(⟦(= λ818 (= λ817 13))⟧) ∧
(⟦(= λ819 (SRC1_OF λ815))⟧) ∧
(⟦(= λ820 (ite λ30 true λ715))⟧) ∧
(⟦(= λ821 (ite λ600 λ820 λ716))⟧) ∧
(⟦(= λ822 (ite λ32 λ821 λ717))⟧) ∧
(⟦(= λ823 (ite λ30 (select IMEM_INIT λ657) λ718))⟧) ∧
(⟦(= λ824 (ite λ603 λ719 λ823))⟧) ∧
(⟦(= λ825 (OPCODE_OF λ824))⟧) ∧
(⟦(= λ826 (= λ825 16))⟧) ∧
(⟦(= λ827 (= λ825 10))⟧) ∧
(⟦(= λ828 (= λ825 17))⟧) ∧
(⟦(= λ829 (ite λ32 (ite λ821 0 (ite (ite (ite λ826 false (ite λ827 true λ828)) true λ826) (DEST_OF λ824) 0)) λ724))⟧) ∧
(⟦(= λ830 (ite λ807 λ725 (ite λ822 0 λ829)))⟧) ∧
(⟦(= λ831 (ite λ30 true λ726))⟧) ∧
(⟦(= λ832 (ite λ600 λ831 λ727))⟧) ∧
(⟦(= λ833 (= λ606 16))⟧) ∧
(⟦(= λ834 (= λ606 17))⟧) ∧
(⟦(= λ835 (= λ606 14))⟧) ∧
(⟦(= λ836 (ite λ32 (ite λ832 0 (ite (ite λ833 false (ite λ834 false (ite λ835 (ite λ598 false true) false))) 31 (ite (ite (ite λ833 false λ834) true λ833) (DEST_OF λ605) 0))) λ731))⟧) ∧
(⟦(= λ837 (ite λ807 λ732 λ836))⟧) ∧
(⟦(= λ838 (ite λ32 λ620 λ733))⟧) ∧
(⟦(= λ839 (ite λ807 λ734 λ838))⟧) ∧
(⟦(= λ840 (ite λ32 λ627 λ735))⟧) ∧
(⟦(= λ841 (ite λ807 λ736 λ840))⟧) ∧
(⟦(= λ842 (ite λ34 (ite (= λ819 0) 0 (ite (= λ830 λ819) 2 (ite (= λ837 λ819) 1 (ite (= λ839 λ819) 4 (ite (= λ841 λ819) 3 5))))) λ737))⟧) ∧
(⟦(= λ843 (ite λ821 false true))⟧) ∧
(⟦(= λ844 (ite λ32 (ite λ827 λ843 false) λ739))⟧) ∧
(⟦(= λ845 (ite λ807 λ740 λ844))⟧) ∧
(⟦(= λ846 (= λ825 11))⟧) ∧
(⟦(= λ847 (ite λ32 (ite λ846 λ843 false) λ742))⟧) ∧
(⟦(= λ848 (ite λ807 λ743 λ847))⟧) ∧
(⟦(= λ849 (SRC1_OF λ824))⟧) ∧
(⟦(= λ850 (ite λ32 (ite (= λ849 0) 0 (ite (= λ849 λ620) 2 (ite (= λ849 λ627) 1 (ite (= λ849 λ629) 4 (ite (= λ849 λ631) 3 5))))) λ745))⟧) ∧
(⟦(= λ851 (= λ850 4))⟧) ∧
(⟦(= λ852 (ite λ32 (select λ687 λ849) λ747))⟧) ∧
(⟦(= λ853 (ite λ807 λ748 (ite (= λ850 0) 0 (ite (= λ850 2) λ654 (ite (= λ850 1) λ665 (ite (ite λ851 λ669 false) λ679 (ite λ851 λ681 (ite (= λ850 3) λ683 λ852))))))))⟧) ∧
(⟦(= λ854 (ite λ32 (SHORT_IMMED_OF λ824) λ749))⟧) ∧
(⟦(= λ855 (SRC2_OF λ824))⟧) ∧
(⟦(= λ856 (ite λ32 (ite (= λ855 0) 0 (ite (= λ855 λ620) 2 (ite (= λ855 λ627) 1 (ite (= λ855 λ629) 4 (ite (= λ855 λ631) 3 5))))) λ751))⟧) ∧
(⟦(= λ857 (= λ856 4))⟧) ∧
(⟦(= λ858 (ite λ32 (select λ687 λ855) λ753))⟧) ∧
(⟦(= λ859 (ite (= λ856 0) 0 (ite (= λ856 2) λ654 (ite (= λ856 1) λ665 (ite (ite λ857 λ669 false) λ679 (ite λ857 λ681 (ite (= λ856 3) λ683 λ858)))))))⟧) ∧
(⟦(= λ860 (ite λ807 λ755 (ite (ite λ32 (ite λ828 true (ite λ827 true λ846)) NO_VALUE14) λ854 λ859)))⟧) ∧
(⟦(= λ861 (ite λ32 λ825 λ756))⟧) ∧
(⟦(= λ862 (ite λ807 λ757 λ861))⟧) ∧
(⟦(= λ863 (ite (ite λ845 true λ848) (plus λ853 λ860) (ALU (ALU_OP_OF λ862) λ853 λ860)))⟧) ∧
(⟦(= λ864 (ite λ34 λ863 λ759))⟧) ∧
(⟦(= λ865 (ite λ32 λ835 λ760))⟧) ∧
(⟦(= λ866 (ite λ807 λ761 λ865))⟧) ∧
(⟦(= λ867 (plus 4 λ491))⟧) ∧
(⟦(= λ868 (ite λ32 (plus 4 λ867) λ763))⟧) ∧
(⟦(= λ869 (ite λ810 λ868 λ764))⟧) ∧
(⟦(= λ870 (ite λ807 λ765 λ607))⟧) ∧
(⟦(= λ871 (ite λ807 λ766 λ689))⟧) ∧
(⟦(= λ872 (ite λ32 λ834 λ767))⟧) ∧
(⟦(= λ873 (ite λ32 (SHORT_IMMED_OF λ605) λ768))⟧) ∧
(⟦(= λ874 (ite λ807 λ769 (ite λ872 λ873 λ694)))⟧) ∧
(⟦(= λ875 (ite λ34 (ite λ866 λ869 (ALU (ALU_OP_OF λ870) λ871 λ874)) λ770))⟧) ∧
(⟦(= λ876 (= λ842 4))⟧) ∧
(⟦(= λ877 (ite λ32 λ635 λ772))⟧) ∧
(⟦(= λ878 (ite λ68 λ877 λ773))⟧) ∧
(⟦(= λ879 (ite λ34 λ878 λ774))⟧) ∧
(⟦(= λ880 (ite λ32 λ638 λ775))⟧) ∧
(⟦(= λ881 (ite λ32 λ653 λ776))⟧) ∧
(⟦(= λ882 (ite λ597 λ777 λ649))⟧) ∧
(⟦(= λ883 (ite λ32 λ882 λ778))⟧) ∧
(⟦(= λ884 (ite (ite λ34 (ite λ880 λ67 false) false) (store λ779 λ881 λ883) λ779))⟧) ∧
(⟦(= λ885 (ite λ32 λ653 λ780))⟧) ∧
(⟦(= λ886 (ite λ72 λ675 λ781))⟧) ∧
(⟦(= λ887 (ite λ32 λ886 λ782))⟧) ∧
(⟦(= λ888 (ite λ34 (select λ884 (ite (ite λ877 λ67 false) λ885 λ887)) λ783))⟧) ∧
(⟦(= λ889 (ite (ite λ878 λ34 false) (ite λ878 λ888 NO_VALUE15) λ784))⟧) ∧
(⟦(= λ890 (ite λ807 λ785 λ654))⟧) ∧
(⟦(= λ891 (ite λ34 λ890 λ786))⟧) ∧
(⟦(= λ892 (ite λ807 λ787 λ665))⟧) ∧
(⟦(= λ893 (ite λ34 λ892 λ788))⟧) ∧
(⟦(= λ894 (ite λ32 λ629 λ789))⟧) ∧
(⟦(= λ895 (ite λ32 λ631 λ790))⟧) ∧
(⟦(= λ896 (ite (ite (ite (= λ895 0) false true) λ68 false) (store λ792 λ895 λ683) λ792))⟧) ∧
(⟦(= λ897 (ite (ite (ite (= λ894 0) false true) λ68 false) (store λ896 λ894 (ite λ669 λ679 λ681)) λ896))⟧) ∧
(⟦(= λ898 (ite λ34 (select λ897 λ819) λ793))⟧) ∧
(⟦(= λ899 (ite (= λ842 0) 0 (ite (= λ842 2) λ864 (ite (= λ842 1) λ875 (ite (ite λ876 λ879 false) λ889 (ite λ876 λ891 (ite (= λ842 3) λ893 λ898)))))))⟧) ∧
(⟦(= λ900 (SRC2_OF λ815))⟧) ∧
(⟦(= λ901 (ite λ34 (ite (= λ900 0) 0 (ite (= λ900 λ830) 2 (ite (= λ900 λ837) 1 (ite (= λ900 λ839) 4 (ite (= λ900 λ841) 3 5))))) λ796))⟧) ∧
(⟦(= λ902 (= λ901 4))⟧) ∧
(⟦(= λ903 (ite λ34 (select λ897 λ900) λ798))⟧) ∧
(⟦(= λ904 (ite (= λ901 0) 0 (ite (= λ901 2) λ864 (ite (= λ901 1) λ875 (ite (ite λ902 λ879 false) λ889 (ite λ902 λ891 (ite (= λ901 3) λ893 λ903)))))))⟧) ∧
(⟦(= λ905 (ite (ite λ809 false true) (ite (ite λ812 false true) (ite (= λ817 12) true (ite (= λ817 14) true (ite λ818 true (ite (= λ817 15) (BRANCH_CONDITION λ899 λ904) false)))) false) false))⟧) ∧
(⟦(= λ906 (ite λ32 λ491 λ801))⟧) ∧
(⟦(= λ907 (ite λ810 λ906 λ802))⟧) ∧
(⟦(= λ908 (ite λ818 λ899 (plus (OFFSET_OF λ815) (plus 4 λ907))))⟧) ∧
(⟦(= λ909 (ite λ66 (ite λ58 λ805 (ite λ800 (plus 4 (plus 4 λ803)) (plus 4 (plus 4 λ804)))) λ804))⟧) ∧
(⟦(= λ910 (ite λ905 λ908 λ909))⟧) ∧
(⟦(= λ911 (ite λ64 (ite λ59 λ806 λ910) λ806))⟧) ∧
(⟦(= λ912 (ite λ66 false true))⟧) ∧
(⟦(= λ913 (ite λ912 λ808 (ite λ707 λ808 λ800)))⟧) ∧
(⟦(= λ914 (ite λ35 λ913 λ809))⟧) ∧
(⟦(= λ915 (ite λ65 λ35 false))⟧) ∧
(⟦(= λ916 (ite λ915 λ58 λ811))⟧) ∧
(⟦(= λ917 (ite λ35 λ916 λ812))⟧) ∧
(⟦(= λ918 (ite λ33 (select IMEM_INIT λ596) λ814))⟧) ∧
(⟦(= λ919 (ite (ite λ58 true λ912) λ815 λ918))⟧) ∧
(⟦(= λ920 (ite λ35 (OPCODE_OF λ919) λ817))⟧) ∧
(⟦(= λ921 (= λ920 13))⟧) ∧
(⟦(= λ922 (SRC1_OF λ919))⟧) ∧
(⟦(= λ923 (ite λ31 true λ820))⟧) ∧
(⟦(= λ924 (ite λ705 λ923 λ821))⟧) ∧
(⟦(= λ925 (ite λ33 λ924 λ822))⟧) ∧
(⟦(= λ926 (ite λ31 (select IMEM_INIT λ762) λ823))⟧) ∧
(⟦(= λ927 (ite λ708 λ824 λ926))⟧) ∧
(⟦(= λ928 (OPCODE_OF λ927))⟧) ∧
(⟦(= λ929 (= λ928 16))⟧) ∧
(⟦(= λ930 (= λ928 10))⟧) ∧
(⟦(= λ931 (= λ928 17))⟧) ∧
(⟦(= λ932 (ite λ33 (ite λ924 0 (ite (ite (ite λ929 false (ite λ930 true λ931)) true λ929) (DEST_OF λ927) 0)) λ829))⟧) ∧
(⟦(= λ933 (ite λ912 λ830 (ite λ925 0 λ932)))⟧) ∧
(⟦(= λ934 (ite λ31 true λ831))⟧) ∧
(⟦(= λ935 (ite λ705 λ934 λ832))⟧) ∧
(⟦(= λ936 (= λ711 16))⟧) ∧
(⟦(= λ937 (= λ711 17))⟧) ∧
(⟦(= λ938 (= λ711 14))⟧) ∧
(⟦(= λ939 (ite λ33 (ite λ935 0 (ite (ite λ936 false (ite λ937 false (ite λ938 (ite λ703 false true) false))) 31 (ite (ite (ite λ936 false λ937) true λ936) (DEST_OF λ710) 0))) λ836))⟧) ∧
(⟦(= λ940 (ite λ912 λ837 λ939))⟧) ∧
(⟦(= λ941 (ite λ33 λ725 λ838))⟧) ∧
(⟦(= λ942 (ite λ912 λ839 λ941))⟧) ∧
(⟦(= λ943 (ite λ33 λ732 λ840))⟧) ∧
(⟦(= λ944 (ite λ912 λ841 λ943))⟧) ∧
(⟦(= λ945 (ite λ35 (ite (= λ922 0) 0 (ite (= λ933 λ922) 2 (ite (= λ940 λ922) 1 (ite (= λ942 λ922) 4 (ite (= λ944 λ922) 3 5))))) λ842))⟧) ∧
(⟦(= λ946 (ite λ924 false true))⟧) ∧
(⟦(= λ947 (ite λ33 (ite λ930 λ946 false) λ844))⟧) ∧
(⟦(= λ948 (ite λ912 λ845 λ947))⟧) ∧
(⟦(= λ949 (= λ928 11))⟧) ∧
(⟦(= λ950 (ite λ33 (ite λ949 λ946 false) λ847))⟧) ∧
(⟦(= λ951 (ite λ912 λ848 λ950))⟧) ∧
(⟦(= λ952 (SRC1_OF λ927))⟧) ∧
(⟦(= λ953 (ite λ33 (ite (= λ952 0) 0 (ite (= λ952 λ725) 2 (ite (= λ952 λ732) 1 (ite (= λ952 λ734) 4 (ite (= λ952 λ736) 3 5))))) λ850))⟧) ∧
(⟦(= λ954 (= λ953 4))⟧) ∧
(⟦(= λ955 (ite λ33 (select λ792 λ952) λ852))⟧) ∧
(⟦(= λ956 (ite λ912 λ853 (ite (= λ953 0) 0 (ite (= λ953 2) λ759 (ite (= λ953 1) λ770 (ite (ite λ954 λ774 false) λ784 (ite λ954 λ786 (ite (= λ953 3) λ788 λ955))))))))⟧) ∧
(⟦(= λ957 (ite λ33 (SHORT_IMMED_OF λ927) λ854))⟧) ∧
(⟦(= λ958 (SRC2_OF λ927))⟧) ∧
(⟦(= λ959 (ite λ33 (ite (= λ958 0) 0 (ite (= λ958 λ725) 2 (ite (= λ958 λ732) 1 (ite (= λ958 λ734) 4 (ite (= λ958 λ736) 3 5))))) λ856))⟧) ∧
(⟦(= λ960 (= λ959 4))⟧) ∧
(⟦(= λ961 (ite λ33 (select λ792 λ958) λ858))⟧) ∧
(⟦(= λ962 (ite (= λ959 0) 0 (ite (= λ959 2) λ759 (ite (= λ959 1) λ770 (ite (ite λ960 λ774 false) λ784 (ite λ960 λ786 (ite (= λ959 3) λ788 λ961)))))))⟧) ∧
(⟦(= λ963 (ite λ912 λ860 (ite (ite λ33 (ite λ931 true (ite λ930 true λ949)) NO_VALUE16) λ957 λ962)))⟧) ∧
(⟦(= λ964 (ite λ33 λ928 λ861))⟧) ∧
(⟦(= λ965 (ite λ912 λ862 λ964))⟧) ∧
(⟦(= λ966 (ite (ite λ948 true λ951) (plus λ956 λ963) (ALU (ALU_OP_OF λ965) λ956 λ963)))⟧) ∧
(⟦(= λ967 (ite λ35 λ966 λ864))⟧) ∧
(⟦(= λ968 (ite λ33 λ938 λ865))⟧) ∧
(⟦(= λ969 (ite λ912 λ866 λ968))⟧) ∧
(⟦(= λ970 (ite λ33 (plus 4 (plus 4 λ596)) λ868))⟧) ∧
(⟦(= λ971 (ite λ915 λ970 λ869))⟧) ∧
(⟦(= λ972 (ite λ912 λ870 λ712))⟧) ∧
(⟦(= λ973 (ite λ912 λ871 λ794))⟧) ∧
(⟦(= λ974 (ite λ33 λ937 λ872))⟧) ∧
(⟦(= λ975 (ite λ33 (SHORT_IMMED_OF λ710) λ873))⟧) ∧
(⟦(= λ976 (ite λ912 λ874 (ite λ974 λ975 λ799)))⟧) ∧
(⟦(= λ977 (ite λ35 (ite λ969 λ971 (ALU (ALU_OP_OF λ972) λ973 λ976)) λ875))⟧) ∧
(⟦(= λ978 (= λ945 4))⟧) ∧
(⟦(= λ979 (ite λ33 λ740 λ877))⟧) ∧
(⟦(= λ980 (ite λ66 λ979 λ878))⟧) ∧
(⟦(= λ981 (ite λ35 λ980 λ879))⟧) ∧
(⟦(= λ982 (ite λ33 λ743 λ880))⟧) ∧
(⟦(= λ983 (ite λ33 λ758 λ881))⟧) ∧
(⟦(= λ984 (ite λ702 λ882 λ754))⟧) ∧
(⟦(= λ985 (ite λ33 λ984 λ883))⟧) ∧
(⟦(= λ986 (ite (ite λ35 (ite λ982 λ65 false) false) (store λ884 λ983 λ985) λ884))⟧) ∧
(⟦(= λ987 (ite λ33 λ758 λ885))⟧) ∧
(⟦(= λ988 (ite λ70 λ780 λ886))⟧) ∧
(⟦(= λ989 (ite λ33 λ988 λ887))⟧) ∧
(⟦(= λ990 (ite λ35 (select λ986 (ite (ite λ979 λ65 false) λ987 λ989)) λ888))⟧) ∧
(⟦(= λ991 (ite (ite λ980 λ35 false) (ite λ980 λ990 NO_VALUE17) λ889))⟧) ∧
(⟦(= λ992 (ite λ912 λ890 λ759))⟧) ∧
(⟦(= λ993 (ite λ35 λ992 λ891))⟧) ∧
(⟦(= λ994 (ite λ912 λ892 λ770))⟧) ∧
(⟦(= λ995 (ite λ35 λ994 λ893))⟧) ∧
(⟦(= λ996 (ite λ33 λ734 λ894))⟧) ∧
(⟦(= λ997 (ite λ33 λ736 λ895))⟧) ∧
(⟦(= λ998 (ite (ite (ite (= λ997 0) false true) λ66 false) (store λ897 λ997 λ788) λ897))⟧) ∧
(⟦(= λ999 (ite (ite (ite (= λ996 0) false true) λ66 false) (store λ998 λ996 (ite λ774 λ784 λ786)) λ998))⟧) ∧
(⟦(= λ1000 (ite λ35 (select λ999 λ922) λ898))⟧) ∧
(⟦(= λ1001 (ite (= λ945 0) 0 (ite (= λ945 2) λ967 (ite (= λ945 1) λ977 (ite (ite λ978 λ981 false) λ991 (ite λ978 λ993 (ite (= λ945 3) λ995 λ1000)))))))⟧) ∧
(⟦(= λ1002 (SRC2_OF λ919))⟧) ∧
(⟦(= λ1003 (ite λ35 (ite (= λ1002 0) 0 (ite (= λ1002 λ933) 2 (ite (= λ1002 λ940) 1 (ite (= λ1002 λ942) 4 (ite (= λ1002 λ944) 3 5))))) λ901))⟧) ∧
(⟦(= λ1004 (= λ1003 4))⟧) ∧
(⟦(= λ1005 (ite λ35 (select λ999 λ1002) λ903))⟧) ∧
(⟦(= λ1006 (ite (ite λ914 false true) (ite (ite λ917 false true) (ite (= λ920 12) true (ite (= λ920 14) true (ite λ921 true (ite (= λ920 15) (BRANCH_CONDITION λ1001 (ite (= λ1003 0) 0 (ite (= λ1003 2) λ967 (ite (= λ1003 1) λ977 (ite (ite λ1004 λ981 false) λ991 (ite λ1004 λ993 (ite (= λ1003 3) λ995 λ1005))))))) false)))) false) false))⟧) ∧
(⟦(= λ1007 (ite λ33 λ596 λ906))⟧) ∧
(⟦(= λ1008 (ite λ915 λ1007 λ907))⟧) ∧
(⟦(= λ1009 (ite λ921 λ1001 (plus (OFFSET_OF λ919) (plus 4 λ1008))))⟧) ∧
(⟦(= λ1010 (ite λ64 (ite λ59 λ910 (ite λ905 (plus 4 (plus 4 λ908)) (plus 4 (plus 4 λ909)))) λ909))⟧) ∧
(⟦(= λ1011 (ite λ1006 λ1009 λ1010))⟧) ∧
(⟦(= λ1012 (ite λ62 (ite λ60 λ911 λ1011) λ911))⟧) ∧
(⟦(= λ1013 (ite λ64 false true))⟧) ∧
(⟦(= λ1014 (ite λ1013 λ913 (ite λ812 λ913 λ905)))⟧) ∧
(⟦(= λ1015 (ite λ63 λ36 false))⟧) ∧
(⟦(= λ1016 (ite λ36 (ite λ1015 λ59 λ916) λ917))⟧) ∧
(⟦(= λ1017 (ite (ite λ59 true λ1013) λ919 (ite λ34 (select IMEM_INIT λ701) λ918)))⟧) ∧
(⟦(= λ1018 (ite λ36 (OPCODE_OF λ1017) λ920))⟧) ∧
(⟦(= λ1019 (= λ1018 13))⟧) ∧
(⟦(= λ1020 (SRC1_OF λ1017))⟧) ∧
(⟦(= λ1021 (ite λ810 (ite λ32 true λ923) λ924))⟧) ∧
(⟦(= λ1022 (ite λ813 λ927 (ite λ32 (select IMEM_INIT λ867) λ926)))⟧) ∧
(⟦(= λ1023 (OPCODE_OF λ1022))⟧) ∧
(⟦(= λ1024 (= λ1023 16))⟧) ∧
(⟦(= λ1025 (= λ1023 10))⟧) ∧
(⟦(= λ1026 (= λ1023 17))⟧) ∧
(⟦(= λ1027 (ite λ1013 λ933 (ite (ite λ34 λ1021 λ925) 0 (ite λ34 (ite λ1021 0 (ite (ite (ite λ1024 false (ite λ1025 true λ1026)) true λ1024) (DEST_OF λ1022) 0)) λ932))))⟧) ∧
(⟦(= λ1028 (= λ816 16))⟧) ∧
(⟦(= λ1029 (= λ816 17))⟧) ∧
(⟦(= λ1030 (= λ816 14))⟧) ∧
(⟦(= λ1031 (ite λ1013 λ940 (ite λ34 (ite (ite λ810 (ite λ32 true λ934) λ935) 0 (ite (ite λ1028 false (ite λ1029 false (ite λ1030 (ite λ808 false true) false))) 31 (ite (ite (ite λ1028 false λ1029) true λ1028) (DEST_OF λ815) 0))) λ939)))⟧) ∧
(⟦(= λ1032 (ite λ1013 λ942 (ite λ34 λ830 λ941)))⟧) ∧
(⟦(= λ1033 (ite λ1013 λ944 (ite λ34 λ837 λ943)))⟧) ∧
(⟦(= λ1034 (ite λ36 (ite (= λ1020 0) 0 (ite (= λ1027 λ1020) 2 (ite (= λ1031 λ1020) 1 (ite (= λ1032 λ1020) 4 (ite (= λ1033 λ1020) 3 5))))) λ945))⟧) ∧
(⟦(= λ1035 (ite λ1021 false true))⟧) ∧
(⟦(= λ1036 (= λ1023 11))⟧) ∧
(⟦(= λ1037 (ite λ1013 λ951 (ite λ34 (ite λ1036 λ1035 false) λ950)))⟧) ∧
(⟦(= λ1038 (SRC1_OF λ1022))⟧) ∧
(⟦(= λ1039 (ite λ34 (ite (= λ1038 0) 0 (ite (= λ1038 λ830) 2 (ite (= λ1038 λ837) 1 (ite (= λ1038 λ839) 4 (ite (= λ1038 λ841) 3 5))))) λ953))⟧) ∧
(⟦(= λ1040 (= λ1039 4))⟧) ∧
(⟦(= λ1041 (ite λ1013 λ956 (ite (= λ1039 0) 0 (ite (= λ1039 2) λ864 (ite (= λ1039 1) λ875 (ite (ite λ1040 λ879 false) λ889 (ite λ1040 λ891 (ite (= λ1039 3) λ893 (ite λ34 (select λ897 λ1038) λ955)))))))))⟧) ∧
(⟦(= λ1042 (SRC2_OF λ1022))⟧) ∧
(⟦(= λ1043 (ite λ34 (ite (= λ1042 0) 0 (ite (= λ1042 λ830) 2 (ite (= λ1042 λ837) 1 (ite (= λ1042 λ839) 4 (ite (= λ1042 λ841) 3 5))))) λ959))⟧) ∧
(⟦(= λ1044 (= λ1043 4))⟧) ∧
(⟦(= λ1045 (ite (= λ1043 0) 0 (ite (= λ1043 2) λ864 (ite (= λ1043 1) λ875 (ite (ite λ1044 λ879 false) λ889 (ite λ1044 λ891 (ite (= λ1043 3) λ893 (ite λ34 (select λ897 λ1042) λ961))))))))⟧) ∧
(⟦(= λ1046 (ite λ1013 λ963 (ite (ite λ34 (ite λ1026 true (ite λ1025 true λ1036)) NO_VALUE18) (ite λ34 (SHORT_IMMED_OF λ1022) λ957) λ1045)))⟧) ∧
(⟦(= λ1047 (ite (ite (ite λ1013 λ948 (ite λ34 (ite λ1025 λ1035 false) λ947)) true λ1037) (plus λ1041 λ1046) (ALU (ALU_OP_OF (ite λ1013 λ965 (ite λ34 λ1023 λ964))) λ1041 λ1046)))⟧) ∧
(⟦(= λ1048 (ite λ36 λ1047 λ967))⟧) ∧
(⟦(= λ1049 (ite λ36 (ite (ite λ1013 λ969 (ite λ34 λ1030 λ968)) (ite λ1015 (ite λ34 (plus 4 (plus 4 λ701)) λ970) λ971) (ALU (ALU_OP_OF (ite λ1013 λ972 λ817)) (ite λ1013 λ973 λ899) (ite λ1013 λ976 (ite (ite λ34 λ1029 λ974) (ite λ34 (SHORT_IMMED_OF λ815) λ975) λ904)))) λ977))⟧) ∧
(⟦(= λ1050 (= λ1034 4))⟧) ∧
(⟦(= λ1051 (ite λ34 λ845 λ979))⟧) ∧
(⟦(= λ1052 (ite λ64 λ1051 λ980))⟧) ∧
(⟦(= λ1053 (ite λ36 λ1052 λ981))⟧) ∧
(⟦(= λ1054 (ite λ34 λ848 λ982))⟧) ∧
(⟦(= λ1055 (ite λ34 λ863 λ983))⟧) ∧
(⟦(= λ1056 (ite λ807 λ984 λ859))⟧) ∧
(⟦(= λ1057 (ite λ34 λ1056 λ985))⟧) ∧
(⟦(= λ1058 (ite (ite λ36 (ite λ1054 λ63 false) false) (store λ986 λ1055 λ1057) λ986))⟧) ∧
(⟦(= λ1059 (ite (ite λ1052 λ36 false) (ite λ1052 (ite λ36 (select λ1058 (ite (ite λ1051 λ63 false) (ite λ34 λ863 λ987) (ite λ34 (ite λ68 λ885 λ988) λ989))) λ990) NO_VALUE19) λ991))⟧) ∧
(⟦(= λ1060 (ite λ36 (ite λ1013 λ992 λ864) λ993))⟧) ∧
(⟦(= λ1061 (ite λ36 (ite λ1013 λ994 λ875) λ995))⟧) ∧
(⟦(= λ1062 (ite λ34 λ839 λ996))⟧) ∧
(⟦(= λ1063 (ite λ34 λ841 λ997))⟧) ∧
(⟦(= λ1064 (ite (ite (ite (= λ1063 0) false true) λ64 false) (store λ999 λ1063 λ893) λ999))⟧) ∧
(⟦(= λ1065 (ite (ite (ite (= λ1062 0) false true) λ64 false) (store λ1064 λ1062 (ite λ879 λ889 λ891)) λ1064))⟧) ∧
(⟦(= λ1066 (ite (= λ1034 0) 0 (ite (= λ1034 2) λ1048 (ite (= λ1034 1) λ1049 (ite (ite λ1050 λ1053 false) λ1059 (ite λ1050 λ1060 (ite (= λ1034 3) λ1061 (ite λ36 (select λ1065 λ1020) λ1000))))))))⟧) ∧
(⟦(= λ1067 (SRC2_OF λ1017))⟧) ∧
(⟦(= λ1068 (ite λ36 (ite (= λ1067 0) 0 (ite (= λ1067 λ1027) 2 (ite (= λ1067 λ1031) 1 (ite (= λ1067 λ1032) 4 (ite (= λ1067 λ1033) 3 5))))) λ1003))⟧) ∧
(⟦(= λ1069 (= λ1068 4))⟧) ∧
(⟦(= λ1070 (ite (ite (ite λ36 λ1014 λ914) false true) (ite (ite λ1016 false true) (ite (= λ1018 12) true (ite (= λ1018 14) true (ite λ1019 true (ite (= λ1018 15) (BRANCH_CONDITION λ1066 (ite (= λ1068 0) 0 (ite (= λ1068 2) λ1048 (ite (= λ1068 1) λ1049 (ite (ite λ1069 λ1053 false) λ1059 (ite λ1069 λ1060 (ite (= λ1068 3) λ1061 (ite λ36 (select λ1065 λ1067) λ1005)))))))) false)))) false) false))⟧) ∧
(⟦(= λ1071 (ite λ50 (ite (ite λ36 true λ60) λ1012 (ite λ1070 (ite λ1019 λ1066 (plus (OFFSET_OF λ1017) (plus 4 (ite λ1015 (ite λ34 λ701 λ1007) λ1008)))) (ite λ62 (ite λ60 λ1011 (ite λ1006 (plus 4 (plus 4 λ1009)) (plus 4 (plus 4 λ1010)))) λ1010))) λ1012))⟧) ∧
(⟦(= λ1072 (plus 4 λ1071))⟧) ∧
(⟦(= λ1073 (select IMEM_INIT λ1072))⟧) ∧
(⟦(= λ1074 (OPCODE_OF λ1073))⟧) ∧
(⟦(= λ1075 (select IMEM_INIT λ1071))⟧) ∧
(⟦(= λ1076 (OPCODE_OF λ1075))⟧) ∧
(⟦(= λ1077 (= λ1076 10))⟧) ∧
(⟦(= λ1078 (ite (ite λ62 false true) λ1014 (ite λ917 λ1014 λ1006)))⟧) ∧
(⟦(= λ1079 (ite (ite λ50 false true) λ1078 (ite λ1016 λ1078 λ1070)))⟧) ∧
(⟦(= λ1080 (ite λ25 λ1079 false))⟧) ∧
(⟦(= λ1081 (= λ1076 12))⟧) ∧
(⟦(= λ1082 (ite λ1079 false true))⟧) ∧
(⟦(= λ1083 (ite λ1082 true λ1080))⟧) ∧
(⟦(= λ1084 (= λ1076 14))⟧) ∧
(⟦(= λ1085 (= λ1076 13))⟧) ∧
(⟦(= λ1086 (= λ1076 15))⟧) ∧
(⟦(= λ1087 (SRC1_OF λ1075))⟧) ∧
(⟦(= λ1088 (ite λ35 λ942 λ1062))⟧) ∧
(⟦(= λ1089 (ite λ36 λ1032 λ1088))⟧) ∧
(⟦(= λ1090 (ite λ35 λ944 λ1063))⟧) ∧
(⟦(= λ1091 (ite λ36 λ1033 λ1090))⟧) ∧
(⟦(= λ1092 (ite (ite (ite (= λ1090 0) false true) λ62 false) (store λ1065 λ1090 λ995) λ1065))⟧) ∧
(⟦(= λ1093 (ite (ite (ite (= λ1088 0) false true) λ62 false) (store λ1092 λ1088 (ite λ981 λ991 λ993)) λ1092))⟧) ∧
(⟦(= λ1094 (ite (ite (ite (= λ1091 0) false true) λ50 false) (store λ1093 λ1091 λ1061) λ1093))⟧) ∧
(⟦(= λ1095 (ite (ite (ite (= λ1089 0) false true) λ50 false) (store λ1094 λ1089 (ite λ1053 λ1059 λ1060)) λ1094))⟧) ∧
(⟦(= λ1096 (ite (= λ1087 0) 0 (select λ1095 λ1087)))⟧) ∧
(⟦(= λ1097 (SRC2_OF λ1075))⟧) ∧
(⟦(= λ1098 (ite (= λ1097 0) 0 (select λ1095 λ1097)))⟧) ∧
(⟦(= λ1099 (ite λ1077 λ1080 (ite λ1081 λ1083 (ite λ1084 λ1083 (ite λ1085 λ1083 (ite λ1086 (ite λ1082 (ite (BRANCH_CONDITION λ1096 λ1098) true λ1080) λ1080) λ1080))))))⟧) ∧
(⟦(= λ1100 (ite λ1082 true λ1099))⟧) ∧
(⟦(= λ1101 (SRC1_OF λ1073))⟧) ∧
(⟦(= λ1102 (DEST_OF λ1075))⟧) ∧
(⟦(= λ1103 (ite (= λ1102 0) false true))⟧) ∧
(⟦(= λ1104 (ite λ35 λ951 λ1054))⟧) ∧
(⟦(= λ1105 (ite λ35 λ966 λ1055))⟧) ∧
(⟦(= λ1106 (ite λ912 λ1056 λ962))⟧) ∧
(⟦(= λ1107 (ite λ35 λ1106 λ1057))⟧) ∧
(⟦(= λ1108 (ite (ite λ37 (ite λ1104 λ61 false) false) (store λ1058 λ1105 λ1107) λ1058))⟧) ∧
(⟦(= λ1109 (SHORT_IMMED_OF λ1075))⟧) ∧
(⟦(= λ1110 (ALU_OP_OF λ1076))⟧) ∧
(⟦(= λ1111 (ite λ1077 (ite λ1103 (store λ1095 λ1102 (select (ite (ite λ38 (ite (ite λ36 λ1037 λ1104) λ49 false) false) (store λ1108 (ite λ36 λ1047 λ1105) (ite λ36 (ite λ1013 λ1106 λ1045) λ1107)) λ1108) (plus λ1096 λ1109))) λ1095) (ite λ1081 λ1095 (ite λ1084 (ite λ1082 (store λ1095 31 (plus 4 (plus 4 (plus 4 λ1072)))) λ1095) (ite λ1085 λ1095 (ite λ1086 λ1095 (ite (= λ1076 17) (ite λ1103 (store λ1095 λ1102 (ALU λ1110 λ1096 λ1109)) λ1095) (ite (= λ1076 16) (ite λ1103 (store λ1095 λ1102 (ALU λ1110 λ1096 λ1098)) λ1095) λ1095))))))))⟧) ∧
(⟦(= λ1112 (SRC2_OF λ1073))⟧) ∧
(⟦(= λ1113 (ite λ38 false true))⟧) ∧
(⟦(= λ1114 (ite λ27 NON_DET_STALL_INIT λ25))⟧) ∧
(⟦(= λ1115 (ite λ28 false λ1114))⟧) ∧
(⟦(= λ1116 (ite λ29 false λ1115))⟧) ∧
(⟦(= λ1117 (ite λ30 false λ1116))⟧) ∧
(⟦(= λ1118 (ite λ31 false λ1117))⟧) ∧
(⟦(= λ1119 (ite λ32 false λ1118))⟧) ∧
(⟦(= λ1120 (ite λ33 false λ1119))⟧) ∧
(⟦(= λ1121 (ite λ34 false λ1120))⟧) ∧
(⟦(= λ1122 (ite λ35 false λ1121))⟧) ∧
(⟦(= λ1123 (ite λ36 false λ1122))⟧) ∧
(⟦(= λ1124 (ite λ37 false λ1123))⟧) ∧
(⟦(= λ1125 (ite λ1123 false true))⟧) ∧
(⟦(= λ1126 (ite λ38 λ1125 false))⟧) ∧
(⟦(= λ1127 (ite λ1126 false true))⟧) ∧
(⟦(= λ1128 (ite λ1122 false true))⟧) ∧
(⟦(= λ1129 (ite λ37 λ1128 false))⟧) ∧
(⟦(= λ1130 (ite λ1129 false true))⟧) ∧
(⟦(= λ1131 (ite λ1121 false true))⟧) ∧
(⟦(= λ1132 (ite λ36 λ1131 false))⟧) ∧
(⟦(= λ1133 (ite λ1132 false true))⟧) ∧
(⟦(= λ1134 (ite λ1120 false true))⟧) ∧
(⟦(= λ1135 (ite λ35 λ1134 false))⟧) ∧
(⟦(= λ1136 (ite λ1135 false true))⟧) ∧
(⟦(= λ1137 (ite λ1119 false true))⟧) ∧
(⟦(= λ1138 (ite λ34 λ1137 false))⟧) ∧
(⟦(= λ1139 (ite λ1138 false true))⟧) ∧
(⟦(= λ1140 (ite λ1118 false true))⟧) ∧
(⟦(= λ1141 (ite λ33 λ1140 false))⟧) ∧
(⟦(= λ1142 (ite λ1141 false true))⟧) ∧
(⟦(= λ1143 (ite λ1117 false true))⟧) ∧
(⟦(= λ1144 (ite λ32 λ1143 false))⟧) ∧
(⟦(= λ1145 (ite λ1144 false true))⟧) ∧
(⟦(= λ1146 (ite λ1116 false true))⟧) ∧
(⟦(= λ1147 (ite λ31 λ1146 false))⟧) ∧
(⟦(= λ1148 (ite λ1147 false true))⟧) ∧
(⟦(= λ1149 (ite λ1115 false true))⟧) ∧
(⟦(= λ1150 (ite λ30 λ1149 false))⟧) ∧
(⟦(= λ1151 (ite λ1150 false true))⟧) ∧
(⟦(= λ1152 (ite λ1114 false true))⟧) ∧
(⟦(= λ1153 (ite λ29 λ1152 false))⟧) ∧
(⟦(= λ1154 (ite λ1153 false true))⟧) ∧
(⟦(= λ1155 (ite λ28 λ26 false))⟧) ∧
(⟦(= λ1156 (ite λ1155 false true))⟧) ∧
(⟦(= λ1157 (ite λ1156 λ118 λ177))⟧) ∧
(⟦(= λ1158 (ite λ1154 λ1157 (ite λ122 λ1157 λ169)))⟧) ∧
(⟦(= λ1159 (ite λ26 λ28 false))⟧) ∧
(⟦(= λ1160 (ite CLOCK_INIT false STALL_S1R_INIT))⟧) ∧
(⟦(= λ1161 (ite λ1159 λ1160 λ121))⟧) ∧
(⟦(= λ1162 (ite λ28 λ1161 λ122))⟧) ∧
(⟦(= λ1163 (ite λ28 λ1157 λ119))⟧) ∧
(⟦(= λ1164 (ite λ1160 true λ1156))⟧) ∧
(⟦(= λ1165 (ite λ1164 λ124 λ184))⟧) ∧
(⟦(= λ1166 (OPCODE_OF λ1165))⟧) ∧
(⟦(= λ1167 (ite λ28 λ1166 λ126))⟧) ∧
(⟦(= λ1168 (= λ1167 13))⟧) ∧
(⟦(= λ1169 (SRC1_OF λ1165))⟧) ∧
(⟦(= λ1170 (ite λ1156 λ129 λ194))⟧) ∧
(⟦(= λ1171 (ite λ1156 λ130 λ199))⟧) ∧
(⟦(= λ1172 (ite λ1156 λ131 λ201))⟧) ∧
(⟦(= λ1173 (ite λ1156 λ132 λ203))⟧) ∧
(⟦(= λ1174 (ite λ28 (ite (= λ1169 0) 0 (ite (= λ1170 λ1169) 2 (ite (= λ1171 λ1169) 1 (ite (= λ1172 λ1169) 4 (ite (= λ1173 λ1169) 3 5))))) λ133))⟧) ∧
(⟦(= λ1175 (ite λ1156 λ134 λ206))⟧) ∧
(⟦(= λ1176 (ite λ1156 λ135 λ209))⟧) ∧
(⟦(= λ1177 (ite λ1156 λ137 λ214))⟧) ∧
(⟦(= λ1178 (ite λ1156 λ140 λ221))⟧) ∧
(⟦(= λ1179 (ite λ1156 λ141 λ223))⟧) ∧
(⟦(= λ1180 (ite (ite λ1175 true λ1176) (plus λ1177 λ1178) (ALU (ALU_OP_OF λ1179) λ1177 λ1178)))⟧) ∧
(⟦(= λ1181 (ite λ28 λ1180 λ143))⟧) ∧
(⟦(= λ1182 (ite λ1156 λ144 λ227))⟧) ∧
(⟦(= λ1183 (ite λ1159 λ229 λ145))⟧) ∧
(⟦(= λ1184 (ite λ1156 λ146 λ95))⟧) ∧
(⟦(= λ1185 (ite λ1156 λ147 λ107))⟧) ∧
(⟦(= λ1186 (ite λ1156 λ148 λ235))⟧) ∧
(⟦(= λ1187 (ite λ28 (ite λ1182 λ1183 (ALU (ALU_OP_OF λ1184) λ1185 λ1186)) λ149))⟧) ∧
(⟦(= λ1188 (= λ1174 4))⟧) ∧
(⟦(= λ1189 (ite λ1155 λ239 λ151))⟧) ∧
(⟦(= λ1190 (ite λ28 λ1189 λ152))⟧) ∧
(⟦(= λ1191 (ite (ite λ28 (ite λ242 λ26 false) false) λ245 λ153))⟧) ∧
(⟦(= λ1192 (ite λ28 (select λ1191 (ite (ite λ239 λ26 false) λ247 λ248)) λ154))⟧) ∧
(⟦(= λ1193 (ite (ite λ1189 λ28 false) (ite λ1189 λ1192 NO_VALUE20) λ155))⟧) ∧
(⟦(= λ1194 (ite λ1156 λ156 λ99))⟧) ∧
(⟦(= λ1195 (ite λ28 λ1194 λ157))⟧) ∧
(⟦(= λ1196 (ite λ1156 λ158 λ100))⟧) ∧
(⟦(= λ1197 (ite λ28 λ1196 λ159))⟧) ∧
(⟦(= λ1198 (ite (ite λ258 λ1155 false) λ259 λ161))⟧) ∧
(⟦(= λ1199 (ite (ite λ256 λ1155 false) (store λ1198 λ255 λ261) λ1198))⟧) ∧
(⟦(= λ1200 (ite λ28 (select λ1199 λ1169) λ162))⟧) ∧
(⟦(= λ1201 (ite (= λ1174 0) 0 (ite (= λ1174 2) λ1181 (ite (= λ1174 1) λ1187 (ite (ite λ1188 λ1190 false) λ1193 (ite λ1188 λ1195 (ite (= λ1174 3) λ1197 λ1200)))))))⟧) ∧
(⟦(= λ1202 (SRC2_OF λ1165))⟧) ∧
(⟦(= λ1203 (ite λ28 (ite (= λ1202 0) 0 (ite (= λ1202 λ1170) 2 (ite (= λ1202 λ1171) 1 (ite (= λ1202 λ1172) 4 (ite (= λ1202 λ1173) 3 5))))) λ165))⟧) ∧
(⟦(= λ1204 (= λ1203 4))⟧) ∧
(⟦(= λ1205 (ite λ28 (select λ1199 λ1202) λ167))⟧) ∧
(⟦(= λ1206 (ite (= λ1203 0) 0 (ite (= λ1203 2) λ1181 (ite (= λ1203 1) λ1187 (ite (ite λ1204 λ1190 false) λ1193 (ite λ1204 λ1195 (ite (= λ1203 3) λ1197 λ1205)))))))⟧) ∧
(⟦(= λ1207 (ite (ite λ1163 false true) (ite (ite λ1162 false true) (ite (= λ1167 12) true (ite (= λ1167 14) true (ite λ1168 true (ite (= λ1167 15) (BRANCH_CONDITION λ1201 λ1206) false)))) false) false))⟧) ∧
(⟦(= λ1208 (ite λ1151 λ1158 (ite λ1162 λ1158 λ1207)))⟧) ∧
(⟦(= λ1209 (ite λ1152 λ29 false))⟧) ∧
(⟦(= λ1210 (ite λ27 false λ1160))⟧) ∧
(⟦(= λ1211 (ite λ1209 λ1210 λ1161))⟧) ∧
(⟦(= λ1212 (ite λ29 λ1211 λ1162))⟧) ∧
(⟦(= λ1213 (ite λ29 λ1158 λ1163))⟧) ∧
(⟦(= λ1214 (ite λ1210 true λ1154))⟧) ∧
(⟦(= λ1215 (ite λ1214 λ1165 λ285))⟧) ∧
(⟦(= λ1216 (OPCODE_OF λ1215))⟧) ∧
(⟦(= λ1217 (ite λ29 λ1216 λ1167))⟧) ∧
(⟦(= λ1218 (= λ1217 13))⟧) ∧
(⟦(= λ1219 (SRC1_OF λ1215))⟧) ∧
(⟦(= λ1220 (ite λ1154 λ1170 λ299))⟧) ∧
(⟦(= λ1221 (ite λ1154 λ1171 λ305))⟧) ∧
(⟦(= λ1222 (ite λ1154 λ1172 λ307))⟧) ∧
(⟦(= λ1223 (ite λ1154 λ1173 λ309))⟧) ∧
(⟦(= λ1224 (ite λ29 (ite (= λ1219 0) 0 (ite (= λ1220 λ1219) 2 (ite (= λ1221 λ1219) 1 (ite (= λ1222 λ1219) 4 (ite (= λ1223 λ1219) 3 5))))) λ1174))⟧) ∧
(⟦(= λ1225 (ite λ1154 λ1175 λ313))⟧) ∧
(⟦(= λ1226 (ite λ1154 λ1176 λ316))⟧) ∧
(⟦(= λ1227 (ite λ1154 λ1177 λ322))⟧) ∧
(⟦(= λ1228 (ite λ1154 λ1178 λ330))⟧) ∧
(⟦(= λ1229 (ite λ1154 λ1179 λ332))⟧) ∧
(⟦(= λ1230 (ite (ite λ1225 true λ1226) (plus λ1227 λ1228) (ALU (ALU_OP_OF λ1229) λ1227 λ1228)))⟧) ∧
(⟦(= λ1231 (ite λ29 λ1230 λ1181))⟧) ∧
(⟦(= λ1232 (ite λ1154 λ1182 λ336))⟧) ∧
(⟦(= λ1233 (ite λ1209 λ339 λ1183))⟧) ∧
(⟦(= λ1234 (ite λ1154 λ1184 λ126))⟧) ∧
(⟦(= λ1235 (ite λ1154 λ1185 λ163))⟧) ∧
(⟦(= λ1236 (ite λ1154 λ1186 λ345))⟧) ∧
(⟦(= λ1237 (ite λ29 (ite λ1232 λ1233 (ALU (ALU_OP_OF λ1234) λ1235 λ1236)) λ1187))⟧) ∧
(⟦(= λ1238 (= λ1224 4))⟧) ∧
(⟦(= λ1239 (ite λ1153 λ349 λ1189))⟧) ∧
(⟦(= λ1240 (ite λ29 λ1239 λ1190))⟧) ∧
(⟦(= λ1241 (ite (ite λ29 (ite λ352 λ1152 false) false) (store λ1191 λ353 λ355) λ1191))⟧) ∧
(⟦(= λ1242 (ite λ29 (select λ1241 (ite (ite λ349 λ1152 false) λ357 λ359)) λ1192))⟧) ∧
(⟦(= λ1243 (ite (ite λ1239 λ29 false) (ite λ1239 λ1242 NO_VALUE21) λ1193))⟧) ∧
(⟦(= λ1244 (ite λ1154 λ1194 λ143))⟧) ∧
(⟦(= λ1245 (ite λ29 λ1244 λ1195))⟧) ∧
(⟦(= λ1246 (ite λ1154 λ1196 λ149))⟧) ∧
(⟦(= λ1247 (ite λ29 λ1246 λ1197))⟧) ∧
(⟦(= λ1248 (ite (ite λ369 λ1153 false) (store λ1199 λ368 λ159) λ1199))⟧) ∧
(⟦(= λ1249 (ite (ite λ367 λ1153 false) (store λ1248 λ366 λ371) λ1248))⟧) ∧
(⟦(= λ1250 (ite λ29 (select λ1249 λ1219) λ1200))⟧) ∧
(⟦(= λ1251 (ite (= λ1224 0) 0 (ite (= λ1224 2) λ1231 (ite (= λ1224 1) λ1237 (ite (ite λ1238 λ1240 false) λ1243 (ite λ1238 λ1245 (ite (= λ1224 3) λ1247 λ1250)))))))⟧) ∧
(⟦(= λ1252 (SRC2_OF λ1215))⟧) ∧
(⟦(= λ1253 (ite λ29 (ite (= λ1252 0) 0 (ite (= λ1252 λ1220) 2 (ite (= λ1252 λ1221) 1 (ite (= λ1252 λ1222) 4 (ite (= λ1252 λ1223) 3 5))))) λ1203))⟧) ∧
(⟦(= λ1254 (= λ1253 4))⟧) ∧
(⟦(= λ1255 (ite λ29 (select λ1249 λ1252) λ1205))⟧) ∧
(⟦(= λ1256 (ite (= λ1253 0) 0 (ite (= λ1253 2) λ1231 (ite (= λ1253 1) λ1237 (ite (ite λ1254 λ1240 false) λ1243 (ite λ1254 λ1245 (ite (= λ1253 3) λ1247 λ1255)))))))⟧) ∧
(⟦(= λ1257 (ite (ite λ1213 false true) (ite (ite λ1212 false true) (ite (= λ1217 12) true (ite (= λ1217 14) true (ite λ1218 true (ite (= λ1217 15) (BRANCH_CONDITION λ1251 λ1256) false)))) false) false))⟧) ∧
(⟦(= λ1258 (ite λ1148 λ1208 (ite λ1212 λ1208 λ1257)))⟧) ∧
(⟦(= λ1259 (ite λ1149 λ30 false))⟧) ∧
(⟦(= λ1260 (ite λ28 true λ1210))⟧) ∧
(⟦(= λ1261 (ite λ1259 λ1260 λ1211))⟧) ∧
(⟦(= λ1262 (ite λ30 λ1261 λ1212))⟧) ∧
(⟦(= λ1263 (ite λ30 λ1208 λ1213))⟧) ∧
(⟦(= λ1264 (ite λ1260 true λ1151))⟧) ∧
(⟦(= λ1265 (ite λ1155 (ite λ1160 λ91 λ115) λ91))⟧) ∧
(⟦(= λ1266 (ite λ28 (select IMEM_INIT λ1265) λ285))⟧) ∧
(⟦(= λ1267 (ite λ1264 λ1215 λ1266))⟧) ∧
(⟦(= λ1268 (OPCODE_OF λ1267))⟧) ∧
(⟦(= λ1269 (ite λ30 λ1268 λ1217))⟧) ∧
(⟦(= λ1270 (= λ1269 13))⟧) ∧
(⟦(= λ1271 (SRC1_OF λ1267))⟧) ∧
(⟦(= λ1272 (ite CLOCK_INIT false BBUBBLE_S1R_INIT))⟧) ∧
(⟦(= λ1273 (ite λ1159 λ1272 λ291))⟧) ∧
(⟦(= λ1274 (ite λ28 λ1273 λ292))⟧) ∧
(⟦(= λ1275 (ite λ1164 λ293 λ403))⟧) ∧
(⟦(= λ1276 (OPCODE_OF λ1275))⟧) ∧
(⟦(= λ1277 (= λ1276 16))⟧) ∧
(⟦(= λ1278 (= λ1276 10))⟧) ∧
(⟦(= λ1279 (= λ1276 17))⟧) ∧
(⟦(= λ1280 (ite λ28 (ite λ1273 0 (ite (ite (ite λ1277 false (ite λ1278 true λ1279)) true λ1277) (DEST_OF λ1275) 0)) λ298))⟧) ∧
(⟦(= λ1281 (ite λ1151 λ1220 (ite λ1274 0 λ1280)))⟧) ∧
(⟦(= λ1282 (ite CLOCK_INIT false ABUBBLE_S1R_INIT))⟧) ∧
(⟦(= λ1283 (ite λ1159 λ1282 λ301))⟧) ∧
(⟦(= λ1284 (= λ1166 16))⟧) ∧
(⟦(= λ1285 (= λ1166 17))⟧) ∧
(⟦(= λ1286 (= λ1166 14))⟧) ∧
(⟦(= λ1287 (ite λ28 (ite λ1283 0 (ite (ite λ1284 false (ite λ1285 false (ite λ1286 (ite λ1157 false true) false))) 31 (ite (ite (ite λ1284 false λ1285) true λ1284) (DEST_OF λ1165) 0))) λ305))⟧) ∧
(⟦(= λ1288 (ite λ1151 λ1221 λ1287))⟧) ∧
(⟦(= λ1289 (ite λ28 λ1170 λ307))⟧) ∧
(⟦(= λ1290 (ite λ1151 λ1222 λ1289))⟧) ∧
(⟦(= λ1291 (ite λ28 λ1171 λ309))⟧) ∧
(⟦(= λ1292 (ite λ1151 λ1223 λ1291))⟧) ∧
(⟦(= λ1293 (ite λ30 (ite (= λ1271 0) 0 (ite (= λ1281 λ1271) 2 (ite (= λ1288 λ1271) 1 (ite (= λ1290 λ1271) 4 (ite (= λ1292 λ1271) 3 5))))) λ1224))⟧) ∧
(⟦(= λ1294 (ite λ1273 false true))⟧) ∧
(⟦(= λ1295 (ite λ28 (ite λ1278 λ1294 false) λ313))⟧) ∧
(⟦(= λ1296 (ite λ1151 λ1225 λ1295))⟧) ∧
(⟦(= λ1297 (= λ1276 11))⟧) ∧
(⟦(= λ1298 (ite λ28 (ite λ1297 λ1294 false) λ316))⟧) ∧
(⟦(= λ1299 (ite λ1151 λ1226 λ1298))⟧) ∧
(⟦(= λ1300 (SRC1_OF λ1275))⟧) ∧
(⟦(= λ1301 (ite λ28 (ite (= λ1300 0) 0 (ite (= λ1300 λ1170) 2 (ite (= λ1300 λ1171) 1 (ite (= λ1300 λ1172) 4 (ite (= λ1300 λ1173) 3 5))))) λ319))⟧) ∧
(⟦(= λ1302 (= λ1301 4))⟧) ∧
(⟦(= λ1303 (ite λ28 (select λ1199 λ1300) λ321))⟧) ∧
(⟦(= λ1304 (ite λ1151 λ1227 (ite (= λ1301 0) 0 (ite (= λ1301 2) λ1181 (ite (= λ1301 1) λ1187 (ite (ite λ1302 λ1190 false) λ1193 (ite λ1302 λ1195 (ite (= λ1301 3) λ1197 λ1303))))))))⟧) ∧
(⟦(= λ1305 (ite λ28 (SHORT_IMMED_OF λ1275) λ324))⟧) ∧
(⟦(= λ1306 (SRC2_OF λ1275))⟧) ∧
(⟦(= λ1307 (ite λ28 (ite (= λ1306 0) 0 (ite (= λ1306 λ1170) 2 (ite (= λ1306 λ1171) 1 (ite (= λ1306 λ1172) 4 (ite (= λ1306 λ1173) 3 5))))) λ326))⟧) ∧
(⟦(= λ1308 (= λ1307 4))⟧) ∧
(⟦(= λ1309 (ite λ28 (select λ1199 λ1306) λ328))⟧) ∧
(⟦(= λ1310 (ite (= λ1307 0) 0 (ite (= λ1307 2) λ1181 (ite (= λ1307 1) λ1187 (ite (ite λ1308 λ1190 false) λ1193 (ite λ1308 λ1195 (ite (= λ1307 3) λ1197 λ1309)))))))⟧) ∧
(⟦(= λ1311 (ite λ1151 λ1228 (ite (ite λ28 (ite λ1279 true (ite λ1278 true λ1297)) NO_VALUE22) λ1305 λ1310)))⟧) ∧
(⟦(= λ1312 (ite λ28 λ1276 λ332))⟧) ∧
(⟦(= λ1313 (ite λ1151 λ1229 λ1312))⟧) ∧
(⟦(= λ1314 (ite (ite λ1296 true λ1299) (plus λ1304 λ1311) (ALU (ALU_OP_OF λ1313) λ1304 λ1311)))⟧) ∧
(⟦(= λ1315 (ite λ30 λ1314 λ1231))⟧) ∧
(⟦(= λ1316 (ite λ28 λ1286 λ336))⟧) ∧
(⟦(= λ1317 (ite λ1151 λ1232 λ1316))⟧) ∧
(⟦(= λ1318 (plus 4 λ1265))⟧) ∧
(⟦(= λ1319 (ite λ28 (plus 4 λ1318) λ339))⟧) ∧
(⟦(= λ1320 (ite λ1259 λ1319 λ1233))⟧) ∧
(⟦(= λ1321 (ite λ1151 λ1234 λ1167))⟧) ∧
(⟦(= λ1322 (ite λ1151 λ1235 λ1201))⟧) ∧
(⟦(= λ1323 (ite λ28 λ1285 λ343))⟧) ∧
(⟦(= λ1324 (ite λ28 (SHORT_IMMED_OF λ1165) λ344))⟧) ∧
(⟦(= λ1325 (ite λ1151 λ1236 (ite λ1323 λ1324 λ1206)))⟧) ∧
(⟦(= λ1326 (ite λ30 (ite λ1317 λ1320 (ALU (ALU_OP_OF λ1321) λ1322 λ1325)) λ1237))⟧) ∧
(⟦(= λ1327 (= λ1293 4))⟧) ∧
(⟦(= λ1328 (ite λ28 λ1175 λ349))⟧) ∧
(⟦(= λ1329 (ite λ1150 λ1328 λ1239))⟧) ∧
(⟦(= λ1330 (ite λ30 λ1329 λ1240))⟧) ∧
(⟦(= λ1331 (ite λ28 λ1176 λ352))⟧) ∧
(⟦(= λ1332 (ite λ28 λ1180 λ353))⟧) ∧
(⟦(= λ1333 (ite λ1156 λ354 λ220))⟧) ∧
(⟦(= λ1334 (ite λ28 λ1333 λ355))⟧) ∧
(⟦(= λ1335 (ite (ite λ30 (ite λ1331 λ1149 false) false) (store λ1241 λ1332 λ1334) λ1241))⟧) ∧
(⟦(= λ1336 (ite λ28 λ1180 λ357))⟧) ∧
(⟦(= λ1337 (ite λ1155 λ247 λ358))⟧) ∧
(⟦(= λ1338 (ite λ28 λ1337 λ359))⟧) ∧
(⟦(= λ1339 (ite λ30 (select λ1335 (ite (ite λ1328 λ1149 false) λ1336 λ1338)) λ1242))⟧) ∧
(⟦(= λ1340 (ite (ite λ1329 λ30 false) (ite λ1329 λ1339 NO_VALUE23) λ1243))⟧) ∧
(⟦(= λ1341 (ite λ1151 λ1244 λ1181))⟧) ∧
(⟦(= λ1342 (ite λ30 λ1341 λ1245))⟧) ∧
(⟦(= λ1343 (ite λ1151 λ1246 λ1187))⟧) ∧
(⟦(= λ1344 (ite λ30 λ1343 λ1247))⟧) ∧
(⟦(= λ1345 (ite λ28 λ1172 λ366))⟧) ∧
(⟦(= λ1346 (ite λ28 λ1173 λ368))⟧) ∧
(⟦(= λ1347 (ite (ite (ite (= λ1346 0) false true) λ1150 false) (store λ1249 λ1346 λ1197) λ1249))⟧) ∧
(⟦(= λ1348 (ite (ite (ite (= λ1345 0) false true) λ1150 false) (store λ1347 λ1345 (ite λ1190 λ1193 λ1195)) λ1347))⟧) ∧
(⟦(= λ1349 (ite λ30 (select λ1348 λ1271) λ1250))⟧) ∧
(⟦(= λ1350 (ite (= λ1293 0) 0 (ite (= λ1293 2) λ1315 (ite (= λ1293 1) λ1326 (ite (ite λ1327 λ1330 false) λ1340 (ite λ1327 λ1342 (ite (= λ1293 3) λ1344 λ1349)))))))⟧) ∧
(⟦(= λ1351 (SRC2_OF λ1267))⟧) ∧
(⟦(= λ1352 (ite λ30 (ite (= λ1351 0) 0 (ite (= λ1351 λ1281) 2 (ite (= λ1351 λ1288) 1 (ite (= λ1351 λ1290) 4 (ite (= λ1351 λ1292) 3 5))))) λ1253))⟧) ∧
(⟦(= λ1353 (= λ1352 4))⟧) ∧
(⟦(= λ1354 (ite λ30 (select λ1348 λ1351) λ1255))⟧) ∧
(⟦(= λ1355 (ite (= λ1352 0) 0 (ite (= λ1352 2) λ1315 (ite (= λ1352 1) λ1326 (ite (ite λ1353 λ1330 false) λ1340 (ite λ1353 λ1342 (ite (= λ1352 3) λ1344 λ1354)))))))⟧) ∧
(⟦(= λ1356 (ite (ite λ1263 false true) (ite (ite λ1262 false true) (ite (= λ1269 12) true (ite (= λ1269 14) true (ite λ1270 true (ite (= λ1269 15) (BRANCH_CONDITION λ1350 λ1355) false)))) false) false))⟧) ∧
(⟦(= λ1357 (ite λ1145 λ1258 (ite λ1262 λ1258 λ1356)))⟧) ∧
(⟦(= λ1358 (ite λ1146 λ31 false))⟧) ∧
(⟦(= λ1359 (ite λ29 true λ1260))⟧) ∧
(⟦(= λ1360 (ite λ1358 λ1359 λ1261))⟧) ∧
(⟦(= λ1361 (ite λ31 λ1360 λ1262))⟧) ∧
(⟦(= λ1362 (ite λ31 λ1258 λ1263))⟧) ∧
(⟦(= λ1363 (ite λ1359 true λ1148))⟧) ∧
(⟦(= λ1364 (ite λ1155 (ite λ1160 λ115 λ172) λ114))⟧) ∧
(⟦(= λ1365 (ite λ169 λ171 λ1364))⟧) ∧
(⟦(= λ1366 (ite λ1153 (ite λ1210 λ1265 λ1365) λ1265))⟧) ∧
(⟦(= λ1367 (ite λ29 (select IMEM_INIT λ1366) λ1266))⟧) ∧
(⟦(= λ1368 (ite λ1363 λ1267 λ1367))⟧) ∧
(⟦(= λ1369 (OPCODE_OF λ1368))⟧) ∧
(⟦(= λ1370 (ite λ31 λ1369 λ1269))⟧) ∧
(⟦(= λ1371 (= λ1370 13))⟧) ∧
(⟦(= λ1372 (SRC1_OF λ1368))⟧) ∧
(⟦(= λ1373 (ite λ27 false λ1272))⟧) ∧
(⟦(= λ1374 (ite λ1209 λ1373 λ1273))⟧) ∧
(⟦(= λ1375 (ite λ29 λ1374 λ1274))⟧) ∧
(⟦(= λ1376 (ite λ1214 λ1275 λ508))⟧) ∧
(⟦(= λ1377 (OPCODE_OF λ1376))⟧) ∧
(⟦(= λ1378 (= λ1377 16))⟧) ∧
(⟦(= λ1379 (= λ1377 10))⟧) ∧
(⟦(= λ1380 (= λ1377 17))⟧) ∧
(⟦(= λ1381 (ite λ29 (ite λ1374 0 (ite (ite (ite λ1378 false (ite λ1379 true λ1380)) true λ1378) (DEST_OF λ1376) 0)) λ1280))⟧) ∧
(⟦(= λ1382 (ite λ1148 λ1281 (ite λ1375 0 λ1381)))⟧) ∧
(⟦(= λ1383 (ite λ27 false λ1282))⟧) ∧
(⟦(= λ1384 (ite λ1209 λ1383 λ1283))⟧) ∧
(⟦(= λ1385 (= λ1216 16))⟧) ∧
(⟦(= λ1386 (= λ1216 17))⟧) ∧
(⟦(= λ1387 (= λ1216 14))⟧) ∧
(⟦(= λ1388 (ite λ29 (ite λ1384 0 (ite (ite λ1385 false (ite λ1386 false (ite λ1387 (ite λ1158 false true) false))) 31 (ite (ite (ite λ1385 false λ1386) true λ1385) (DEST_OF λ1215) 0))) λ1287))⟧) ∧
(⟦(= λ1389 (ite λ1148 λ1288 λ1388))⟧) ∧
(⟦(= λ1390 (ite λ29 λ1220 λ1289))⟧) ∧
(⟦(= λ1391 (ite λ1148 λ1290 λ1390))⟧) ∧
(⟦(= λ1392 (ite λ29 λ1221 λ1291))⟧) ∧
(⟦(= λ1393 (ite λ1148 λ1292 λ1392))⟧) ∧
(⟦(= λ1394 (ite λ31 (ite (= λ1372 0) 0 (ite (= λ1382 λ1372) 2 (ite (= λ1389 λ1372) 1 (ite (= λ1391 λ1372) 4 (ite (= λ1393 λ1372) 3 5))))) λ1293))⟧) ∧
(⟦(= λ1395 (ite λ1374 false true))⟧) ∧
(⟦(= λ1396 (ite λ29 (ite λ1379 λ1395 false) λ1295))⟧) ∧
(⟦(= λ1397 (ite λ1148 λ1296 λ1396))⟧) ∧
(⟦(= λ1398 (= λ1377 11))⟧) ∧
(⟦(= λ1399 (ite λ29 (ite λ1398 λ1395 false) λ1298))⟧) ∧
(⟦(= λ1400 (ite λ1148 λ1299 λ1399))⟧) ∧
(⟦(= λ1401 (SRC1_OF λ1376))⟧) ∧
(⟦(= λ1402 (ite λ29 (ite (= λ1401 0) 0 (ite (= λ1401 λ1220) 2 (ite (= λ1401 λ1221) 1 (ite (= λ1401 λ1222) 4 (ite (= λ1401 λ1223) 3 5))))) λ1301))⟧) ∧
(⟦(= λ1403 (= λ1402 4))⟧) ∧
(⟦(= λ1404 (ite λ29 (select λ1249 λ1401) λ1303))⟧) ∧
(⟦(= λ1405 (ite λ1148 λ1304 (ite (= λ1402 0) 0 (ite (= λ1402 2) λ1231 (ite (= λ1402 1) λ1237 (ite (ite λ1403 λ1240 false) λ1243 (ite λ1403 λ1245 (ite (= λ1402 3) λ1247 λ1404))))))))⟧) ∧
(⟦(= λ1406 (ite λ29 (SHORT_IMMED_OF λ1376) λ1305))⟧) ∧
(⟦(= λ1407 (SRC2_OF λ1376))⟧) ∧
(⟦(= λ1408 (ite λ29 (ite (= λ1407 0) 0 (ite (= λ1407 λ1220) 2 (ite (= λ1407 λ1221) 1 (ite (= λ1407 λ1222) 4 (ite (= λ1407 λ1223) 3 5))))) λ1307))⟧) ∧
(⟦(= λ1409 (= λ1408 4))⟧) ∧
(⟦(= λ1410 (ite λ29 (select λ1249 λ1407) λ1309))⟧) ∧
(⟦(= λ1411 (ite (= λ1408 0) 0 (ite (= λ1408 2) λ1231 (ite (= λ1408 1) λ1237 (ite (ite λ1409 λ1240 false) λ1243 (ite λ1409 λ1245 (ite (= λ1408 3) λ1247 λ1410)))))))⟧) ∧
(⟦(= λ1412 (ite λ1148 λ1311 (ite (ite λ29 (ite λ1380 true (ite λ1379 true λ1398)) NO_VALUE24) λ1406 λ1411)))⟧) ∧
(⟦(= λ1413 (ite λ29 λ1377 λ1312))⟧) ∧
(⟦(= λ1414 (ite λ1148 λ1313 λ1413))⟧) ∧
(⟦(= λ1415 (ite (ite λ1397 true λ1400) (plus λ1405 λ1412) (ALU (ALU_OP_OF λ1414) λ1405 λ1412)))⟧) ∧
(⟦(= λ1416 (ite λ31 λ1415 λ1315))⟧) ∧
(⟦(= λ1417 (ite λ29 λ1387 λ1316))⟧) ∧
(⟦(= λ1418 (ite λ1148 λ1317 λ1417))⟧) ∧
(⟦(= λ1419 (plus 4 λ1366))⟧) ∧
(⟦(= λ1420 (ite λ29 (plus 4 λ1419) λ1319))⟧) ∧
(⟦(= λ1421 (ite λ1358 λ1420 λ1320))⟧) ∧
(⟦(= λ1422 (ite λ1148 λ1321 λ1217))⟧) ∧
(⟦(= λ1423 (ite λ1148 λ1322 λ1251))⟧) ∧
(⟦(= λ1424 (ite λ29 λ1386 λ1323))⟧) ∧
(⟦(= λ1425 (ite λ29 (SHORT_IMMED_OF λ1215) λ1324))⟧) ∧
(⟦(= λ1426 (ite λ1148 λ1325 (ite λ1424 λ1425 λ1256)))⟧) ∧
(⟦(= λ1427 (ite λ31 (ite λ1418 λ1421 (ALU (ALU_OP_OF λ1422) λ1423 λ1426)) λ1326))⟧) ∧
(⟦(= λ1428 (= λ1394 4))⟧) ∧
(⟦(= λ1429 (ite λ29 λ1225 λ1328))⟧) ∧
(⟦(= λ1430 (ite λ1147 λ1429 λ1329))⟧) ∧
(⟦(= λ1431 (ite λ31 λ1430 λ1330))⟧) ∧
(⟦(= λ1432 (ite λ29 λ1226 λ1331))⟧) ∧
(⟦(= λ1433 (ite λ29 λ1230 λ1332))⟧) ∧
(⟦(= λ1434 (ite λ1154 λ1333 λ329))⟧) ∧
(⟦(= λ1435 (ite λ29 λ1434 λ1334))⟧) ∧
(⟦(= λ1436 (ite (ite λ31 (ite λ1432 λ1146 false) false) (store λ1335 λ1433 λ1435) λ1335))⟧) ∧
(⟦(= λ1437 (ite λ29 λ1230 λ1336))⟧) ∧
(⟦(= λ1438 (ite λ1153 λ357 λ1337))⟧) ∧
(⟦(= λ1439 (ite λ29 λ1438 λ1338))⟧) ∧
(⟦(= λ1440 (ite λ31 (select λ1436 (ite (ite λ1429 λ1146 false) λ1437 λ1439)) λ1339))⟧) ∧
(⟦(= λ1441 (ite (ite λ1430 λ31 false) (ite λ1430 λ1440 NO_VALUE25) λ1340))⟧) ∧
(⟦(= λ1442 (ite λ1148 λ1341 λ1231))⟧) ∧
(⟦(= λ1443 (ite λ31 λ1442 λ1342))⟧) ∧
(⟦(= λ1444 (ite λ1148 λ1343 λ1237))⟧) ∧
(⟦(= λ1445 (ite λ31 λ1444 λ1344))⟧) ∧
(⟦(= λ1446 (ite λ29 λ1222 λ1345))⟧) ∧
(⟦(= λ1447 (ite λ29 λ1223 λ1346))⟧) ∧
(⟦(= λ1448 (ite (ite (ite (= λ1447 0) false true) λ1147 false) (store λ1348 λ1447 λ1247) λ1348))⟧) ∧
(⟦(= λ1449 (ite (ite (ite (= λ1446 0) false true) λ1147 false) (store λ1448 λ1446 (ite λ1240 λ1243 λ1245)) λ1448))⟧) ∧
(⟦(= λ1450 (ite λ31 (select λ1449 λ1372) λ1349))⟧) ∧
(⟦(= λ1451 (ite (= λ1394 0) 0 (ite (= λ1394 2) λ1416 (ite (= λ1394 1) λ1427 (ite (ite λ1428 λ1431 false) λ1441 (ite λ1428 λ1443 (ite (= λ1394 3) λ1445 λ1450)))))))⟧) ∧
(⟦(= λ1452 (SRC2_OF λ1368))⟧) ∧
(⟦(= λ1453 (ite λ31 (ite (= λ1452 0) 0 (ite (= λ1452 λ1382) 2 (ite (= λ1452 λ1389) 1 (ite (= λ1452 λ1391) 4 (ite (= λ1452 λ1393) 3 5))))) λ1352))⟧) ∧
(⟦(= λ1454 (= λ1453 4))⟧) ∧
(⟦(= λ1455 (ite λ31 (select λ1449 λ1452) λ1354))⟧) ∧
(⟦(= λ1456 (ite (= λ1453 0) 0 (ite (= λ1453 2) λ1416 (ite (= λ1453 1) λ1427 (ite (ite λ1454 λ1431 false) λ1441 (ite λ1454 λ1443 (ite (= λ1453 3) λ1445 λ1455)))))))⟧) ∧
(⟦(= λ1457 (ite (ite λ1362 false true) (ite (ite λ1361 false true) (ite (= λ1370 12) true (ite (= λ1370 14) true (ite λ1371 true (ite (= λ1370 15) (BRANCH_CONDITION λ1451 λ1456) false)))) false) false))⟧) ∧
(⟦(= λ1458 (ite λ1142 λ1357 (ite λ1361 λ1357 λ1457)))⟧) ∧
(⟦(= λ1459 (ite λ1143 λ32 false))⟧) ∧
(⟦(= λ1460 (ite λ30 true λ1359))⟧) ∧
(⟦(= λ1461 (ite λ1459 λ1460 λ1360))⟧) ∧
(⟦(= λ1462 (ite λ32 λ1461 λ1361))⟧) ∧
(⟦(= λ1463 (ite λ32 λ1357 λ1362))⟧) ∧
(⟦(= λ1464 (ite λ1460 true λ1145))⟧) ∧
(⟦(= λ1465 (ite λ1159 λ271 λ170))⟧) ∧
(⟦(= λ1466 (ite λ1168 λ1201 (plus (OFFSET_OF λ1165) (plus 4 λ1465))))⟧) ∧
(⟦(= λ1467 (ite λ1153 (ite λ1210 λ1365 (ite λ169 λ274 (plus 4 (plus 4 λ1364)))) λ1364))⟧) ∧
(⟦(= λ1468 (ite λ1207 λ1466 λ1467))⟧) ∧
(⟦(= λ1469 (ite λ1150 (ite λ1260 λ1366 λ1468) λ1366))⟧) ∧
(⟦(= λ1470 (ite λ30 (select IMEM_INIT λ1469) λ1367))⟧) ∧
(⟦(= λ1471 (ite λ1464 λ1368 λ1470))⟧) ∧
(⟦(= λ1472 (OPCODE_OF λ1471))⟧) ∧
(⟦(= λ1473 (ite λ32 λ1472 λ1370))⟧) ∧
(⟦(= λ1474 (= λ1473 13))⟧) ∧
(⟦(= λ1475 (SRC1_OF λ1471))⟧) ∧
(⟦(= λ1476 (ite λ28 true λ1373))⟧) ∧
(⟦(= λ1477 (ite λ1259 λ1476 λ1374))⟧) ∧
(⟦(= λ1478 (ite λ30 λ1477 λ1375))⟧) ∧
(⟦(= λ1479 (ite λ28 (select IMEM_INIT λ1318) λ508))⟧) ∧
(⟦(= λ1480 (ite λ1264 λ1376 λ1479))⟧) ∧
(⟦(= λ1481 (OPCODE_OF λ1480))⟧) ∧
(⟦(= λ1482 (= λ1481 16))⟧) ∧
(⟦(= λ1483 (= λ1481 10))⟧) ∧
(⟦(= λ1484 (= λ1481 17))⟧) ∧
(⟦(= λ1485 (ite λ30 (ite λ1477 0 (ite (ite (ite λ1482 false (ite λ1483 true λ1484)) true λ1482) (DEST_OF λ1480) 0)) λ1381))⟧) ∧
(⟦(= λ1486 (ite λ1145 λ1382 (ite λ1478 0 λ1485)))⟧) ∧
(⟦(= λ1487 (ite λ28 true λ1383))⟧) ∧
(⟦(= λ1488 (ite λ1259 λ1487 λ1384))⟧) ∧
(⟦(= λ1489 (= λ1268 16))⟧) ∧
(⟦(= λ1490 (= λ1268 17))⟧) ∧
(⟦(= λ1491 (= λ1268 14))⟧) ∧
(⟦(= λ1492 (ite λ30 (ite λ1488 0 (ite (ite λ1489 false (ite λ1490 false (ite λ1491 (ite λ1208 false true) false))) 31 (ite (ite (ite λ1489 false λ1490) true λ1489) (DEST_OF λ1267) 0))) λ1388))⟧) ∧
(⟦(= λ1493 (ite λ1145 λ1389 λ1492))⟧) ∧
(⟦(= λ1494 (ite λ30 λ1281 λ1390))⟧) ∧
(⟦(= λ1495 (ite λ1145 λ1391 λ1494))⟧) ∧
(⟦(= λ1496 (ite λ30 λ1288 λ1392))⟧) ∧
(⟦(= λ1497 (ite λ1145 λ1393 λ1496))⟧) ∧
(⟦(= λ1498 (ite λ32 (ite (= λ1475 0) 0 (ite (= λ1486 λ1475) 2 (ite (= λ1493 λ1475) 1 (ite (= λ1495 λ1475) 4 (ite (= λ1497 λ1475) 3 5))))) λ1394))⟧) ∧
(⟦(= λ1499 (ite λ1477 false true))⟧) ∧
(⟦(= λ1500 (ite λ30 (ite λ1483 λ1499 false) λ1396))⟧) ∧
(⟦(= λ1501 (ite λ1145 λ1397 λ1500))⟧) ∧
(⟦(= λ1502 (= λ1481 11))⟧) ∧
(⟦(= λ1503 (ite λ30 (ite λ1502 λ1499 false) λ1399))⟧) ∧
(⟦(= λ1504 (ite λ1145 λ1400 λ1503))⟧) ∧
(⟦(= λ1505 (SRC1_OF λ1480))⟧) ∧
(⟦(= λ1506 (ite λ30 (ite (= λ1505 0) 0 (ite (= λ1505 λ1281) 2 (ite (= λ1505 λ1288) 1 (ite (= λ1505 λ1290) 4 (ite (= λ1505 λ1292) 3 5))))) λ1402))⟧) ∧
(⟦(= λ1507 (= λ1506 4))⟧) ∧
(⟦(= λ1508 (ite λ30 (select λ1348 λ1505) λ1404))⟧) ∧
(⟦(= λ1509 (ite λ1145 λ1405 (ite (= λ1506 0) 0 (ite (= λ1506 2) λ1315 (ite (= λ1506 1) λ1326 (ite (ite λ1507 λ1330 false) λ1340 (ite λ1507 λ1342 (ite (= λ1506 3) λ1344 λ1508))))))))⟧) ∧
(⟦(= λ1510 (ite λ30 (SHORT_IMMED_OF λ1480) λ1406))⟧) ∧
(⟦(= λ1511 (SRC2_OF λ1480))⟧) ∧
(⟦(= λ1512 (ite λ30 (ite (= λ1511 0) 0 (ite (= λ1511 λ1281) 2 (ite (= λ1511 λ1288) 1 (ite (= λ1511 λ1290) 4 (ite (= λ1511 λ1292) 3 5))))) λ1408))⟧) ∧
(⟦(= λ1513 (= λ1512 4))⟧) ∧
(⟦(= λ1514 (ite λ30 (select λ1348 λ1511) λ1410))⟧) ∧
(⟦(= λ1515 (ite (= λ1512 0) 0 (ite (= λ1512 2) λ1315 (ite (= λ1512 1) λ1326 (ite (ite λ1513 λ1330 false) λ1340 (ite λ1513 λ1342 (ite (= λ1512 3) λ1344 λ1514)))))))⟧) ∧
(⟦(= λ1516 (ite λ1145 λ1412 (ite (ite λ30 (ite λ1484 true (ite λ1483 true λ1502)) NO_VALUE26) λ1510 λ1515)))⟧) ∧
(⟦(= λ1517 (ite λ30 λ1481 λ1413))⟧) ∧
(⟦(= λ1518 (ite λ1145 λ1414 λ1517))⟧) ∧
(⟦(= λ1519 (ite (ite λ1501 true λ1504) (plus λ1509 λ1516) (ALU (ALU_OP_OF λ1518) λ1509 λ1516)))⟧) ∧
(⟦(= λ1520 (ite λ32 λ1519 λ1416))⟧) ∧
(⟦(= λ1521 (ite λ30 λ1491 λ1417))⟧) ∧
(⟦(= λ1522 (ite λ1145 λ1418 λ1521))⟧) ∧
(⟦(= λ1523 (plus 4 λ1469))⟧) ∧
(⟦(= λ1524 (ite λ30 (plus 4 λ1523) λ1420))⟧) ∧
(⟦(= λ1525 (ite λ1459 λ1524 λ1421))⟧) ∧
(⟦(= λ1526 (ite λ1145 λ1422 λ1269))⟧) ∧
(⟦(= λ1527 (ite λ1145 λ1423 λ1350))⟧) ∧
(⟦(= λ1528 (ite λ30 λ1490 λ1424))⟧) ∧
(⟦(= λ1529 (ite λ30 (SHORT_IMMED_OF λ1267) λ1425))⟧) ∧
(⟦(= λ1530 (ite λ1145 λ1426 (ite λ1528 λ1529 λ1355)))⟧) ∧
(⟦(= λ1531 (ite λ32 (ite λ1522 λ1525 (ALU (ALU_OP_OF λ1526) λ1527 λ1530)) λ1427))⟧) ∧
(⟦(= λ1532 (= λ1498 4))⟧) ∧
(⟦(= λ1533 (ite λ30 λ1296 λ1429))⟧) ∧
(⟦(= λ1534 (ite λ1144 λ1533 λ1430))⟧) ∧
(⟦(= λ1535 (ite λ32 λ1534 λ1431))⟧) ∧
(⟦(= λ1536 (ite λ30 λ1299 λ1432))⟧) ∧
(⟦(= λ1537 (ite λ30 λ1314 λ1433))⟧) ∧
(⟦(= λ1538 (ite λ1151 λ1434 λ1310))⟧) ∧
(⟦(= λ1539 (ite λ30 λ1538 λ1435))⟧) ∧
(⟦(= λ1540 (ite (ite λ32 (ite λ1536 λ1143 false) false) (store λ1436 λ1537 λ1539) λ1436))⟧) ∧
(⟦(= λ1541 (ite λ30 λ1314 λ1437))⟧) ∧
(⟦(= λ1542 (ite λ1150 λ1336 λ1438))⟧) ∧
(⟦(= λ1543 (ite λ30 λ1542 λ1439))⟧) ∧
(⟦(= λ1544 (ite λ32 (select λ1540 (ite (ite λ1533 λ1143 false) λ1541 λ1543)) λ1440))⟧) ∧
(⟦(= λ1545 (ite (ite λ1534 λ32 false) (ite λ1534 λ1544 NO_VALUE27) λ1441))⟧) ∧
(⟦(= λ1546 (ite λ1145 λ1442 λ1315))⟧) ∧
(⟦(= λ1547 (ite λ32 λ1546 λ1443))⟧) ∧
(⟦(= λ1548 (ite λ1145 λ1444 λ1326))⟧) ∧
(⟦(= λ1549 (ite λ32 λ1548 λ1445))⟧) ∧
(⟦(= λ1550 (ite λ30 λ1290 λ1446))⟧) ∧
(⟦(= λ1551 (ite λ30 λ1292 λ1447))⟧) ∧
(⟦(= λ1552 (ite (ite (ite (= λ1551 0) false true) λ1144 false) (store λ1449 λ1551 λ1344) λ1449))⟧) ∧
(⟦(= λ1553 (ite (ite (ite (= λ1550 0) false true) λ1144 false) (store λ1552 λ1550 (ite λ1330 λ1340 λ1342)) λ1552))⟧) ∧
(⟦(= λ1554 (ite λ32 (select λ1553 λ1475) λ1450))⟧) ∧
(⟦(= λ1555 (ite (= λ1498 0) 0 (ite (= λ1498 2) λ1520 (ite (= λ1498 1) λ1531 (ite (ite λ1532 λ1535 false) λ1545 (ite λ1532 λ1547 (ite (= λ1498 3) λ1549 λ1554)))))))⟧) ∧
(⟦(= λ1556 (SRC2_OF λ1471))⟧) ∧
(⟦(= λ1557 (ite λ32 (ite (= λ1556 0) 0 (ite (= λ1556 λ1486) 2 (ite (= λ1556 λ1493) 1 (ite (= λ1556 λ1495) 4 (ite (= λ1556 λ1497) 3 5))))) λ1453))⟧) ∧
(⟦(= λ1558 (= λ1557 4))⟧) ∧
(⟦(= λ1559 (ite λ32 (select λ1553 λ1556) λ1455))⟧) ∧
(⟦(= λ1560 (ite (= λ1557 0) 0 (ite (= λ1557 2) λ1520 (ite (= λ1557 1) λ1531 (ite (ite λ1558 λ1535 false) λ1545 (ite λ1558 λ1547 (ite (= λ1557 3) λ1549 λ1559)))))))⟧) ∧
(⟦(= λ1561 (ite (ite λ1463 false true) (ite (ite λ1462 false true) (ite (= λ1473 12) true (ite (= λ1473 14) true (ite λ1474 true (ite (= λ1473 15) (BRANCH_CONDITION λ1555 λ1560) false)))) false) false))⟧) ∧
(⟦(= λ1562 (ite λ1139 λ1458 (ite λ1462 λ1458 λ1561)))⟧) ∧
(⟦(= λ1563 (ite λ1140 λ33 false))⟧) ∧
(⟦(= λ1564 (ite λ31 true λ1460))⟧) ∧
(⟦(= λ1565 (ite λ1563 λ1564 λ1461))⟧) ∧
(⟦(= λ1566 (ite λ33 λ1565 λ1462))⟧) ∧
(⟦(= λ1567 (ite λ33 λ1458 λ1463))⟧) ∧
(⟦(= λ1568 (ite λ1564 true λ1142))⟧) ∧
(⟦(= λ1569 (ite λ1209 λ381 λ1465))⟧) ∧
(⟦(= λ1570 (ite λ1218 λ1251 (plus (OFFSET_OF λ1215) (plus 4 λ1569))))⟧) ∧
(⟦(= λ1571 (ite λ1150 (ite λ1260 λ1468 (ite λ1207 (plus 4 (plus 4 λ1466)) (plus 4 (plus 4 λ1467)))) λ1467))⟧) ∧
(⟦(= λ1572 (ite λ1257 λ1570 λ1571))⟧) ∧
(⟦(= λ1573 (ite λ1147 (ite λ1359 λ1469 λ1572) λ1469))⟧) ∧
(⟦(= λ1574 (ite λ31 (select IMEM_INIT λ1573) λ1470))⟧) ∧
(⟦(= λ1575 (ite λ1568 λ1471 λ1574))⟧) ∧
(⟦(= λ1576 (OPCODE_OF λ1575))⟧) ∧
(⟦(= λ1577 (ite λ33 λ1576 λ1473))⟧) ∧
(⟦(= λ1578 (= λ1577 13))⟧) ∧
(⟦(= λ1579 (SRC1_OF λ1575))⟧) ∧
(⟦(= λ1580 (ite λ29 true λ1476))⟧) ∧
(⟦(= λ1581 (ite λ1358 λ1580 λ1477))⟧) ∧
(⟦(= λ1582 (ite λ31 λ1581 λ1478))⟧) ∧
(⟦(= λ1583 (ite λ29 (select IMEM_INIT λ1419) λ1479))⟧) ∧
(⟦(= λ1584 (ite λ1363 λ1480 λ1583))⟧) ∧
(⟦(= λ1585 (OPCODE_OF λ1584))⟧) ∧
(⟦(= λ1586 (= λ1585 16))⟧) ∧
(⟦(= λ1587 (= λ1585 10))⟧) ∧
(⟦(= λ1588 (= λ1585 17))⟧) ∧
(⟦(= λ1589 (ite λ31 (ite λ1581 0 (ite (ite (ite λ1586 false (ite λ1587 true λ1588)) true λ1586) (DEST_OF λ1584) 0)) λ1485))⟧) ∧
(⟦(= λ1590 (ite λ1142 λ1486 (ite λ1582 0 λ1589)))⟧) ∧
(⟦(= λ1591 (ite λ29 true λ1487))⟧) ∧
(⟦(= λ1592 (ite λ1358 λ1591 λ1488))⟧) ∧
(⟦(= λ1593 (= λ1369 16))⟧) ∧
(⟦(= λ1594 (= λ1369 17))⟧) ∧
(⟦(= λ1595 (= λ1369 14))⟧) ∧
(⟦(= λ1596 (ite λ31 (ite λ1592 0 (ite (ite λ1593 false (ite λ1594 false (ite λ1595 (ite λ1258 false true) false))) 31 (ite (ite (ite λ1593 false λ1594) true λ1593) (DEST_OF λ1368) 0))) λ1492))⟧) ∧
(⟦(= λ1597 (ite λ1142 λ1493 λ1596))⟧) ∧
(⟦(= λ1598 (ite λ31 λ1382 λ1494))⟧) ∧
(⟦(= λ1599 (ite λ1142 λ1495 λ1598))⟧) ∧
(⟦(= λ1600 (ite λ31 λ1389 λ1496))⟧) ∧
(⟦(= λ1601 (ite λ1142 λ1497 λ1600))⟧) ∧
(⟦(= λ1602 (ite λ33 (ite (= λ1579 0) 0 (ite (= λ1590 λ1579) 2 (ite (= λ1597 λ1579) 1 (ite (= λ1599 λ1579) 4 (ite (= λ1601 λ1579) 3 5))))) λ1498))⟧) ∧
(⟦(= λ1603 (ite λ1581 false true))⟧) ∧
(⟦(= λ1604 (ite λ31 (ite λ1587 λ1603 false) λ1500))⟧) ∧
(⟦(= λ1605 (ite λ1142 λ1501 λ1604))⟧) ∧
(⟦(= λ1606 (= λ1585 11))⟧) ∧
(⟦(= λ1607 (ite λ31 (ite λ1606 λ1603 false) λ1503))⟧) ∧
(⟦(= λ1608 (ite λ1142 λ1504 λ1607))⟧) ∧
(⟦(= λ1609 (SRC1_OF λ1584))⟧) ∧
(⟦(= λ1610 (ite λ31 (ite (= λ1609 0) 0 (ite (= λ1609 λ1382) 2 (ite (= λ1609 λ1389) 1 (ite (= λ1609 λ1391) 4 (ite (= λ1609 λ1393) 3 5))))) λ1506))⟧) ∧
(⟦(= λ1611 (= λ1610 4))⟧) ∧
(⟦(= λ1612 (ite λ31 (select λ1449 λ1609) λ1508))⟧) ∧
(⟦(= λ1613 (ite λ1142 λ1509 (ite (= λ1610 0) 0 (ite (= λ1610 2) λ1416 (ite (= λ1610 1) λ1427 (ite (ite λ1611 λ1431 false) λ1441 (ite λ1611 λ1443 (ite (= λ1610 3) λ1445 λ1612))))))))⟧) ∧
(⟦(= λ1614 (ite λ31 (SHORT_IMMED_OF λ1584) λ1510))⟧) ∧
(⟦(= λ1615 (SRC2_OF λ1584))⟧) ∧
(⟦(= λ1616 (ite λ31 (ite (= λ1615 0) 0 (ite (= λ1615 λ1382) 2 (ite (= λ1615 λ1389) 1 (ite (= λ1615 λ1391) 4 (ite (= λ1615 λ1393) 3 5))))) λ1512))⟧) ∧
(⟦(= λ1617 (= λ1616 4))⟧) ∧
(⟦(= λ1618 (ite λ31 (select λ1449 λ1615) λ1514))⟧) ∧
(⟦(= λ1619 (ite (= λ1616 0) 0 (ite (= λ1616 2) λ1416 (ite (= λ1616 1) λ1427 (ite (ite λ1617 λ1431 false) λ1441 (ite λ1617 λ1443 (ite (= λ1616 3) λ1445 λ1618)))))))⟧) ∧
(⟦(= λ1620 (ite λ1142 λ1516 (ite (ite λ31 (ite λ1588 true (ite λ1587 true λ1606)) NO_VALUE28) λ1614 λ1619)))⟧) ∧
(⟦(= λ1621 (ite λ31 λ1585 λ1517))⟧) ∧
(⟦(= λ1622 (ite λ1142 λ1518 λ1621))⟧) ∧
(⟦(= λ1623 (ite (ite λ1605 true λ1608) (plus λ1613 λ1620) (ALU (ALU_OP_OF λ1622) λ1613 λ1620)))⟧) ∧
(⟦(= λ1624 (ite λ33 λ1623 λ1520))⟧) ∧
(⟦(= λ1625 (ite λ31 λ1595 λ1521))⟧) ∧
(⟦(= λ1626 (ite λ1142 λ1522 λ1625))⟧) ∧
(⟦(= λ1627 (plus 4 λ1573))⟧) ∧
(⟦(= λ1628 (ite λ31 (plus 4 λ1627) λ1524))⟧) ∧
(⟦(= λ1629 (ite λ1563 λ1628 λ1525))⟧) ∧
(⟦(= λ1630 (ite λ1142 λ1526 λ1370))⟧) ∧
(⟦(= λ1631 (ite λ1142 λ1527 λ1451))⟧) ∧
(⟦(= λ1632 (ite λ31 λ1594 λ1528))⟧) ∧
(⟦(= λ1633 (ite λ31 (SHORT_IMMED_OF λ1368) λ1529))⟧) ∧
(⟦(= λ1634 (ite λ1142 λ1530 (ite λ1632 λ1633 λ1456)))⟧) ∧
(⟦(= λ1635 (ite λ33 (ite λ1626 λ1629 (ALU (ALU_OP_OF λ1630) λ1631 λ1634)) λ1531))⟧) ∧
(⟦(= λ1636 (= λ1602 4))⟧) ∧
(⟦(= λ1637 (ite λ31 λ1397 λ1533))⟧) ∧
(⟦(= λ1638 (ite λ1141 λ1637 λ1534))⟧) ∧
(⟦(= λ1639 (ite λ33 λ1638 λ1535))⟧) ∧
(⟦(= λ1640 (ite λ31 λ1400 λ1536))⟧) ∧
(⟦(= λ1641 (ite λ31 λ1415 λ1537))⟧) ∧
(⟦(= λ1642 (ite λ1148 λ1538 λ1411))⟧) ∧
(⟦(= λ1643 (ite λ31 λ1642 λ1539))⟧) ∧
(⟦(= λ1644 (ite (ite λ33 (ite λ1640 λ1140 false) false) (store λ1540 λ1641 λ1643) λ1540))⟧) ∧
(⟦(= λ1645 (ite λ31 λ1415 λ1541))⟧) ∧
(⟦(= λ1646 (ite λ1147 λ1437 λ1542))⟧) ∧
(⟦(= λ1647 (ite λ31 λ1646 λ1543))⟧) ∧
(⟦(= λ1648 (ite λ33 (select λ1644 (ite (ite λ1637 λ1140 false) λ1645 λ1647)) λ1544))⟧) ∧
(⟦(= λ1649 (ite (ite λ1638 λ33 false) (ite λ1638 λ1648 NO_VALUE29) λ1545))⟧) ∧
(⟦(= λ1650 (ite λ1142 λ1546 λ1416))⟧) ∧
(⟦(= λ1651 (ite λ33 λ1650 λ1547))⟧) ∧
(⟦(= λ1652 (ite λ1142 λ1548 λ1427))⟧) ∧
(⟦(= λ1653 (ite λ33 λ1652 λ1549))⟧) ∧
(⟦(= λ1654 (ite λ31 λ1391 λ1550))⟧) ∧
(⟦(= λ1655 (ite λ31 λ1393 λ1551))⟧) ∧
(⟦(= λ1656 (ite (ite (ite (= λ1655 0) false true) λ1141 false) (store λ1553 λ1655 λ1445) λ1553))⟧) ∧
(⟦(= λ1657 (ite (ite (ite (= λ1654 0) false true) λ1141 false) (store λ1656 λ1654 (ite λ1431 λ1441 λ1443)) λ1656))⟧) ∧
(⟦(= λ1658 (ite λ33 (select λ1657 λ1579) λ1554))⟧) ∧
(⟦(= λ1659 (ite (= λ1602 0) 0 (ite (= λ1602 2) λ1624 (ite (= λ1602 1) λ1635 (ite (ite λ1636 λ1639 false) λ1649 (ite λ1636 λ1651 (ite (= λ1602 3) λ1653 λ1658)))))))⟧) ∧
(⟦(= λ1660 (SRC2_OF λ1575))⟧) ∧
(⟦(= λ1661 (ite λ33 (ite (= λ1660 0) 0 (ite (= λ1660 λ1590) 2 (ite (= λ1660 λ1597) 1 (ite (= λ1660 λ1599) 4 (ite (= λ1660 λ1601) 3 5))))) λ1557))⟧) ∧
(⟦(= λ1662 (= λ1661 4))⟧) ∧
(⟦(= λ1663 (ite λ33 (select λ1657 λ1660) λ1559))⟧) ∧
(⟦(= λ1664 (ite (= λ1661 0) 0 (ite (= λ1661 2) λ1624 (ite (= λ1661 1) λ1635 (ite (ite λ1662 λ1639 false) λ1649 (ite λ1662 λ1651 (ite (= λ1661 3) λ1653 λ1663)))))))⟧) ∧
(⟦(= λ1665 (ite (ite λ1567 false true) (ite (ite λ1566 false true) (ite (= λ1577 12) true (ite (= λ1577 14) true (ite λ1578 true (ite (= λ1577 15) (BRANCH_CONDITION λ1659 λ1664) false)))) false) false))⟧) ∧
(⟦(= λ1666 (ite λ1136 λ1562 (ite λ1566 λ1562 λ1665)))⟧) ∧
(⟦(= λ1667 (ite λ1137 λ34 false))⟧) ∧
(⟦(= λ1668 (ite λ32 true λ1564))⟧) ∧
(⟦(= λ1669 (ite λ1667 λ1668 λ1565))⟧) ∧
(⟦(= λ1670 (ite λ34 λ1669 λ1566))⟧) ∧
(⟦(= λ1671 (ite λ34 λ1562 λ1567))⟧) ∧
(⟦(= λ1672 (ite λ1668 true λ1139))⟧) ∧
(⟦(= λ1673 (ite λ28 λ1265 λ381))⟧) ∧
(⟦(= λ1674 (ite λ1259 λ1673 λ1569))⟧) ∧
(⟦(= λ1675 (ite λ1270 λ1350 (plus (OFFSET_OF λ1267) (plus 4 λ1674))))⟧) ∧
(⟦(= λ1676 (ite λ1147 (ite λ1359 λ1572 (ite λ1257 (plus 4 (plus 4 λ1570)) (plus 4 (plus 4 λ1571)))) λ1571))⟧) ∧
(⟦(= λ1677 (ite λ1356 λ1675 λ1676))⟧) ∧
(⟦(= λ1678 (ite λ1144 (ite λ1460 λ1573 λ1677) λ1573))⟧) ∧
(⟦(= λ1679 (ite λ32 (select IMEM_INIT λ1678) λ1574))⟧) ∧
(⟦(= λ1680 (ite λ1672 λ1575 λ1679))⟧) ∧
(⟦(= λ1681 (OPCODE_OF λ1680))⟧) ∧
(⟦(= λ1682 (ite λ34 λ1681 λ1577))⟧) ∧
(⟦(= λ1683 (= λ1682 13))⟧) ∧
(⟦(= λ1684 (SRC1_OF λ1680))⟧) ∧
(⟦(= λ1685 (ite λ30 true λ1580))⟧) ∧
(⟦(= λ1686 (ite λ1459 λ1685 λ1581))⟧) ∧
(⟦(= λ1687 (ite λ32 λ1686 λ1582))⟧) ∧
(⟦(= λ1688 (ite λ30 (select IMEM_INIT λ1523) λ1583))⟧) ∧
(⟦(= λ1689 (ite λ1464 λ1584 λ1688))⟧) ∧
(⟦(= λ1690 (OPCODE_OF λ1689))⟧) ∧
(⟦(= λ1691 (= λ1690 16))⟧) ∧
(⟦(= λ1692 (= λ1690 10))⟧) ∧
(⟦(= λ1693 (= λ1690 17))⟧) ∧
(⟦(= λ1694 (ite λ32 (ite λ1686 0 (ite (ite (ite λ1691 false (ite λ1692 true λ1693)) true λ1691) (DEST_OF λ1689) 0)) λ1589))⟧) ∧
(⟦(= λ1695 (ite λ1139 λ1590 (ite λ1687 0 λ1694)))⟧) ∧
(⟦(= λ1696 (ite λ30 true λ1591))⟧) ∧
(⟦(= λ1697 (ite λ1459 λ1696 λ1592))⟧) ∧
(⟦(= λ1698 (= λ1472 16))⟧) ∧
(⟦(= λ1699 (= λ1472 17))⟧) ∧
(⟦(= λ1700 (= λ1472 14))⟧) ∧
(⟦(= λ1701 (ite λ32 (ite λ1697 0 (ite (ite λ1698 false (ite λ1699 false (ite λ1700 (ite λ1357 false true) false))) 31 (ite (ite (ite λ1698 false λ1699) true λ1698) (DEST_OF λ1471) 0))) λ1596))⟧) ∧
(⟦(= λ1702 (ite λ1139 λ1597 λ1701))⟧) ∧
(⟦(= λ1703 (ite λ32 λ1486 λ1598))⟧) ∧
(⟦(= λ1704 (ite λ1139 λ1599 λ1703))⟧) ∧
(⟦(= λ1705 (ite λ32 λ1493 λ1600))⟧) ∧
(⟦(= λ1706 (ite λ1139 λ1601 λ1705))⟧) ∧
(⟦(= λ1707 (ite λ34 (ite (= λ1684 0) 0 (ite (= λ1695 λ1684) 2 (ite (= λ1702 λ1684) 1 (ite (= λ1704 λ1684) 4 (ite (= λ1706 λ1684) 3 5))))) λ1602))⟧) ∧
(⟦(= λ1708 (ite λ1686 false true))⟧) ∧
(⟦(= λ1709 (ite λ32 (ite λ1692 λ1708 false) λ1604))⟧) ∧
(⟦(= λ1710 (ite λ1139 λ1605 λ1709))⟧) ∧
(⟦(= λ1711 (= λ1690 11))⟧) ∧
(⟦(= λ1712 (ite λ32 (ite λ1711 λ1708 false) λ1607))⟧) ∧
(⟦(= λ1713 (ite λ1139 λ1608 λ1712))⟧) ∧
(⟦(= λ1714 (SRC1_OF λ1689))⟧) ∧
(⟦(= λ1715 (ite λ32 (ite (= λ1714 0) 0 (ite (= λ1714 λ1486) 2 (ite (= λ1714 λ1493) 1 (ite (= λ1714 λ1495) 4 (ite (= λ1714 λ1497) 3 5))))) λ1610))⟧) ∧
(⟦(= λ1716 (= λ1715 4))⟧) ∧
(⟦(= λ1717 (ite λ32 (select λ1553 λ1714) λ1612))⟧) ∧
(⟦(= λ1718 (ite λ1139 λ1613 (ite (= λ1715 0) 0 (ite (= λ1715 2) λ1520 (ite (= λ1715 1) λ1531 (ite (ite λ1716 λ1535 false) λ1545 (ite λ1716 λ1547 (ite (= λ1715 3) λ1549 λ1717))))))))⟧) ∧
(⟦(= λ1719 (ite λ32 (SHORT_IMMED_OF λ1689) λ1614))⟧) ∧
(⟦(= λ1720 (SRC2_OF λ1689))⟧) ∧
(⟦(= λ1721 (ite λ32 (ite (= λ1720 0) 0 (ite (= λ1720 λ1486) 2 (ite (= λ1720 λ1493) 1 (ite (= λ1720 λ1495) 4 (ite (= λ1720 λ1497) 3 5))))) λ1616))⟧) ∧
(⟦(= λ1722 (= λ1721 4))⟧) ∧
(⟦(= λ1723 (ite λ32 (select λ1553 λ1720) λ1618))⟧) ∧
(⟦(= λ1724 (ite (= λ1721 0) 0 (ite (= λ1721 2) λ1520 (ite (= λ1721 1) λ1531 (ite (ite λ1722 λ1535 false) λ1545 (ite λ1722 λ1547 (ite (= λ1721 3) λ1549 λ1723)))))))⟧) ∧
(⟦(= λ1725 (ite λ1139 λ1620 (ite (ite λ32 (ite λ1693 true (ite λ1692 true λ1711)) NO_VALUE30) λ1719 λ1724)))⟧) ∧
(⟦(= λ1726 (ite λ32 λ1690 λ1621))⟧) ∧
(⟦(= λ1727 (ite λ1139 λ1622 λ1726))⟧) ∧
(⟦(= λ1728 (ite (ite λ1710 true λ1713) (plus λ1718 λ1725) (ALU (ALU_OP_OF λ1727) λ1718 λ1725)))⟧) ∧
(⟦(= λ1729 (ite λ34 λ1728 λ1624))⟧) ∧
(⟦(= λ1730 (ite λ32 λ1700 λ1625))⟧) ∧
(⟦(= λ1731 (ite λ1139 λ1626 λ1730))⟧) ∧
(⟦(= λ1732 (plus 4 λ1678))⟧) ∧
(⟦(= λ1733 (ite λ32 (plus 4 λ1732) λ1628))⟧) ∧
(⟦(= λ1734 (ite λ1667 λ1733 λ1629))⟧) ∧
(⟦(= λ1735 (ite λ1139 λ1630 λ1473))⟧) ∧
(⟦(= λ1736 (ite λ1139 λ1631 λ1555))⟧) ∧
(⟦(= λ1737 (ite λ32 λ1699 λ1632))⟧) ∧
(⟦(= λ1738 (ite λ32 (SHORT_IMMED_OF λ1471) λ1633))⟧) ∧
(⟦(= λ1739 (ite λ1139 λ1634 (ite λ1737 λ1738 λ1560)))⟧) ∧
(⟦(= λ1740 (ite λ34 (ite λ1731 λ1734 (ALU (ALU_OP_OF λ1735) λ1736 λ1739)) λ1635))⟧) ∧
(⟦(= λ1741 (= λ1707 4))⟧) ∧
(⟦(= λ1742 (ite λ32 λ1501 λ1637))⟧) ∧
(⟦(= λ1743 (ite λ1138 λ1742 λ1638))⟧) ∧
(⟦(= λ1744 (ite λ34 λ1743 λ1639))⟧) ∧
(⟦(= λ1745 (ite λ32 λ1504 λ1640))⟧) ∧
(⟦(= λ1746 (ite λ32 λ1519 λ1641))⟧) ∧
(⟦(= λ1747 (ite λ1145 λ1642 λ1515))⟧) ∧
(⟦(= λ1748 (ite λ32 λ1747 λ1643))⟧) ∧
(⟦(= λ1749 (ite (ite λ34 (ite λ1745 λ1137 false) false) (store λ1644 λ1746 λ1748) λ1644))⟧) ∧
(⟦(= λ1750 (ite λ32 λ1519 λ1645))⟧) ∧
(⟦(= λ1751 (ite λ1144 λ1541 λ1646))⟧) ∧
(⟦(= λ1752 (ite λ32 λ1751 λ1647))⟧) ∧
(⟦(= λ1753 (ite λ34 (select λ1749 (ite (ite λ1742 λ1137 false) λ1750 λ1752)) λ1648))⟧) ∧
(⟦(= λ1754 (ite (ite λ1743 λ34 false) (ite λ1743 λ1753 NO_VALUE31) λ1649))⟧) ∧
(⟦(= λ1755 (ite λ1139 λ1650 λ1520))⟧) ∧
(⟦(= λ1756 (ite λ34 λ1755 λ1651))⟧) ∧
(⟦(= λ1757 (ite λ1139 λ1652 λ1531))⟧) ∧
(⟦(= λ1758 (ite λ34 λ1757 λ1653))⟧) ∧
(⟦(= λ1759 (ite λ32 λ1495 λ1654))⟧) ∧
(⟦(= λ1760 (ite λ32 λ1497 λ1655))⟧) ∧
(⟦(= λ1761 (ite (ite (ite (= λ1760 0) false true) λ1138 false) (store λ1657 λ1760 λ1549) λ1657))⟧) ∧
(⟦(= λ1762 (ite (ite (ite (= λ1759 0) false true) λ1138 false) (store λ1761 λ1759 (ite λ1535 λ1545 λ1547)) λ1761))⟧) ∧
(⟦(= λ1763 (ite λ34 (select λ1762 λ1684) λ1658))⟧) ∧
(⟦(= λ1764 (ite (= λ1707 0) 0 (ite (= λ1707 2) λ1729 (ite (= λ1707 1) λ1740 (ite (ite λ1741 λ1744 false) λ1754 (ite λ1741 λ1756 (ite (= λ1707 3) λ1758 λ1763)))))))⟧) ∧
(⟦(= λ1765 (SRC2_OF λ1680))⟧) ∧
(⟦(= λ1766 (ite λ34 (ite (= λ1765 0) 0 (ite (= λ1765 λ1695) 2 (ite (= λ1765 λ1702) 1 (ite (= λ1765 λ1704) 4 (ite (= λ1765 λ1706) 3 5))))) λ1661))⟧) ∧
(⟦(= λ1767 (= λ1766 4))⟧) ∧
(⟦(= λ1768 (ite λ34 (select λ1762 λ1765) λ1663))⟧) ∧
(⟦(= λ1769 (ite (= λ1766 0) 0 (ite (= λ1766 2) λ1729 (ite (= λ1766 1) λ1740 (ite (ite λ1767 λ1744 false) λ1754 (ite λ1767 λ1756 (ite (= λ1766 3) λ1758 λ1768)))))))⟧) ∧
(⟦(= λ1770 (ite (ite λ1671 false true) (ite (ite λ1670 false true) (ite (= λ1682 12) true (ite (= λ1682 14) true (ite λ1683 true (ite (= λ1682 15) (BRANCH_CONDITION λ1764 λ1769) false)))) false) false))⟧) ∧
(⟦(= λ1771 (ite λ1133 λ1666 (ite λ1670 λ1666 λ1770)))⟧) ∧
(⟦(= λ1772 (ite λ1134 λ35 false))⟧) ∧
(⟦(= λ1773 (ite λ33 true λ1668))⟧) ∧
(⟦(= λ1774 (ite λ1772 λ1773 λ1669))⟧) ∧
(⟦(= λ1775 (ite λ35 λ1774 λ1670))⟧) ∧
(⟦(= λ1776 (ite λ35 λ1666 λ1671))⟧) ∧
(⟦(= λ1777 (ite λ1773 true λ1136))⟧) ∧
(⟦(= λ1778 (ite λ29 λ1366 λ1673))⟧) ∧
(⟦(= λ1779 (ite λ1358 λ1778 λ1674))⟧) ∧
(⟦(= λ1780 (ite λ1371 λ1451 (plus (OFFSET_OF λ1368) (plus 4 λ1779))))⟧) ∧
(⟦(= λ1781 (ite λ1144 (ite λ1460 λ1677 (ite λ1356 (plus 4 (plus 4 λ1675)) (plus 4 (plus 4 λ1676)))) λ1676))⟧) ∧
(⟦(= λ1782 (ite λ1457 λ1780 λ1781))⟧) ∧
(⟦(= λ1783 (ite λ1141 (ite λ1564 λ1678 λ1782) λ1678))⟧) ∧
(⟦(= λ1784 (ite λ33 (select IMEM_INIT λ1783) λ1679))⟧) ∧
(⟦(= λ1785 (ite λ1777 λ1680 λ1784))⟧) ∧
(⟦(= λ1786 (OPCODE_OF λ1785))⟧) ∧
(⟦(= λ1787 (ite λ35 λ1786 λ1682))⟧) ∧
(⟦(= λ1788 (SRC1_OF λ1785))⟧) ∧
(⟦(= λ1789 (ite λ31 true λ1685))⟧) ∧
(⟦(= λ1790 (ite λ1563 λ1789 λ1686))⟧) ∧
(⟦(= λ1791 (ite λ33 λ1790 λ1687))⟧) ∧
(⟦(= λ1792 (ite λ31 (select IMEM_INIT λ1627) λ1688))⟧) ∧
(⟦(= λ1793 (ite λ1568 λ1689 λ1792))⟧) ∧
(⟦(= λ1794 (OPCODE_OF λ1793))⟧) ∧
(⟦(= λ1795 (= λ1794 16))⟧) ∧
(⟦(= λ1796 (= λ1794 10))⟧) ∧
(⟦(= λ1797 (= λ1794 17))⟧) ∧
(⟦(= λ1798 (ite λ33 (ite λ1790 0 (ite (ite (ite λ1795 false (ite λ1796 true λ1797)) true λ1795) (DEST_OF λ1793) 0)) λ1694))⟧) ∧
(⟦(= λ1799 (ite λ1136 λ1695 (ite λ1791 0 λ1798)))⟧) ∧
(⟦(= λ1800 (ite λ31 true λ1696))⟧) ∧
(⟦(= λ1801 (ite λ1563 λ1800 λ1697))⟧) ∧
(⟦(= λ1802 (= λ1576 16))⟧) ∧
(⟦(= λ1803 (= λ1576 17))⟧) ∧
(⟦(= λ1804 (= λ1576 14))⟧) ∧
(⟦(= λ1805 (ite λ33 (ite λ1801 0 (ite (ite λ1802 false (ite λ1803 false (ite λ1804 (ite λ1458 false true) false))) 31 (ite (ite (ite λ1802 false λ1803) true λ1802) (DEST_OF λ1575) 0))) λ1701))⟧) ∧
(⟦(= λ1806 (ite λ1136 λ1702 λ1805))⟧) ∧
(⟦(= λ1807 (ite λ33 λ1590 λ1703))⟧) ∧
(⟦(= λ1808 (ite λ1136 λ1704 λ1807))⟧) ∧
(⟦(= λ1809 (ite λ33 λ1597 λ1705))⟧) ∧
(⟦(= λ1810 (ite λ1136 λ1706 λ1809))⟧) ∧
(⟦(= λ1811 (ite λ35 (ite (= λ1788 0) 0 (ite (= λ1799 λ1788) 2 (ite (= λ1806 λ1788) 1 (ite (= λ1808 λ1788) 4 (ite (= λ1810 λ1788) 3 5))))) λ1707))⟧) ∧
(⟦(= λ1812 (ite λ1790 false true))⟧) ∧
(⟦(= λ1813 (ite λ33 (ite λ1796 λ1812 false) λ1709))⟧) ∧
(⟦(= λ1814 (ite λ1136 λ1710 λ1813))⟧) ∧
(⟦(= λ1815 (= λ1794 11))⟧) ∧
(⟦(= λ1816 (ite λ33 (ite λ1815 λ1812 false) λ1712))⟧) ∧
(⟦(= λ1817 (ite λ1136 λ1713 λ1816))⟧) ∧
(⟦(= λ1818 (SRC1_OF λ1793))⟧) ∧
(⟦(= λ1819 (ite λ33 (ite (= λ1818 0) 0 (ite (= λ1818 λ1590) 2 (ite (= λ1818 λ1597) 1 (ite (= λ1818 λ1599) 4 (ite (= λ1818 λ1601) 3 5))))) λ1715))⟧) ∧
(⟦(= λ1820 (= λ1819 4))⟧) ∧
(⟦(= λ1821 (ite λ33 (select λ1657 λ1818) λ1717))⟧) ∧
(⟦(= λ1822 (ite λ1136 λ1718 (ite (= λ1819 0) 0 (ite (= λ1819 2) λ1624 (ite (= λ1819 1) λ1635 (ite (ite λ1820 λ1639 false) λ1649 (ite λ1820 λ1651 (ite (= λ1819 3) λ1653 λ1821))))))))⟧) ∧
(⟦(= λ1823 (ite λ33 (SHORT_IMMED_OF λ1793) λ1719))⟧) ∧
(⟦(= λ1824 (SRC2_OF λ1793))⟧) ∧
(⟦(= λ1825 (ite λ33 (ite (= λ1824 0) 0 (ite (= λ1824 λ1590) 2 (ite (= λ1824 λ1597) 1 (ite (= λ1824 λ1599) 4 (ite (= λ1824 λ1601) 3 5))))) λ1721))⟧) ∧
(⟦(= λ1826 (= λ1825 4))⟧) ∧
(⟦(= λ1827 (ite λ33 (select λ1657 λ1824) λ1723))⟧) ∧
(⟦(= λ1828 (ite (= λ1825 0) 0 (ite (= λ1825 2) λ1624 (ite (= λ1825 1) λ1635 (ite (ite λ1826 λ1639 false) λ1649 (ite λ1826 λ1651 (ite (= λ1825 3) λ1653 λ1827)))))))⟧) ∧
(⟦(= λ1829 (ite λ1136 λ1725 (ite (ite λ33 (ite λ1797 true (ite λ1796 true λ1815)) NO_VALUE32) λ1823 λ1828)))⟧) ∧
(⟦(= λ1830 (ite λ33 λ1794 λ1726))⟧) ∧
(⟦(= λ1831 (ite λ1136 λ1727 λ1830))⟧) ∧
(⟦(= λ1832 (ite (ite λ1814 true λ1817) (plus λ1822 λ1829) (ALU (ALU_OP_OF λ1831) λ1822 λ1829)))⟧) ∧
(⟦(= λ1833 (ite λ35 λ1832 λ1729))⟧) ∧
(⟦(= λ1834 (ite λ33 λ1804 λ1730))⟧) ∧
(⟦(= λ1835 (ite λ1136 λ1731 λ1834))⟧) ∧
(⟦(= λ1836 (plus 4 λ1783))⟧) ∧
(⟦(= λ1837 (ite λ33 (plus 4 λ1836) λ1733))⟧) ∧
(⟦(= λ1838 (ite λ1772 λ1837 λ1734))⟧) ∧
(⟦(= λ1839 (ite λ1136 λ1735 λ1577))⟧) ∧
(⟦(= λ1840 (ite λ1136 λ1736 λ1659))⟧) ∧
(⟦(= λ1841 (ite λ33 λ1803 λ1737))⟧) ∧
(⟦(= λ1842 (ite λ33 (SHORT_IMMED_OF λ1575) λ1738))⟧) ∧
(⟦(= λ1843 (ite λ1136 λ1739 (ite λ1841 λ1842 λ1664)))⟧) ∧
(⟦(= λ1844 (ite λ35 (ite λ1835 λ1838 (ALU (ALU_OP_OF λ1839) λ1840 λ1843)) λ1740))⟧) ∧
(⟦(= λ1845 (= λ1811 4))⟧) ∧
(⟦(= λ1846 (ite λ33 λ1605 λ1742))⟧) ∧
(⟦(= λ1847 (ite λ1135 λ1846 λ1743))⟧) ∧
(⟦(= λ1848 (ite λ35 λ1847 λ1744))⟧) ∧
(⟦(= λ1849 (ite λ33 λ1608 λ1745))⟧) ∧
(⟦(= λ1850 (ite λ33 λ1623 λ1746))⟧) ∧
(⟦(= λ1851 (ite λ1142 λ1747 λ1619))⟧) ∧
(⟦(= λ1852 (ite λ33 λ1851 λ1748))⟧) ∧
(⟦(= λ1853 (ite (ite λ35 (ite λ1849 λ1134 false) false) (store λ1749 λ1850 λ1852) λ1749))⟧) ∧
(⟦(= λ1854 (ite λ33 λ1623 λ1750))⟧) ∧
(⟦(= λ1855 (ite λ1141 λ1645 λ1751))⟧) ∧
(⟦(= λ1856 (ite λ33 λ1855 λ1752))⟧) ∧
(⟦(= λ1857 (ite λ35 (select λ1853 (ite (ite λ1846 λ1134 false) λ1854 λ1856)) λ1753))⟧) ∧
(⟦(= λ1858 (ite (ite λ1847 λ35 false) (ite λ1847 λ1857 NO_VALUE33) λ1754))⟧) ∧
(⟦(= λ1859 (ite λ1136 λ1755 λ1624))⟧) ∧
(⟦(= λ1860 (ite λ35 λ1859 λ1756))⟧) ∧
(⟦(= λ1861 (ite λ1136 λ1757 λ1635))⟧) ∧
(⟦(= λ1862 (ite λ35 λ1861 λ1758))⟧) ∧
(⟦(= λ1863 (ite λ33 λ1599 λ1759))⟧) ∧
(⟦(= λ1864 (ite λ33 λ1601 λ1760))⟧) ∧
(⟦(= λ1865 (ite (ite (ite (= λ1864 0) false true) λ1135 false) (store λ1762 λ1864 λ1653) λ1762))⟧) ∧
(⟦(= λ1866 (ite (ite (ite (= λ1863 0) false true) λ1135 false) (store λ1865 λ1863 (ite λ1639 λ1649 λ1651)) λ1865))⟧) ∧
(⟦(= λ1867 (ite λ35 (select λ1866 λ1788) λ1763))⟧) ∧
(⟦(= λ1868 (ite (= λ1811 0) 0 (ite (= λ1811 2) λ1833 (ite (= λ1811 1) λ1844 (ite (ite λ1845 λ1848 false) λ1858 (ite λ1845 λ1860 (ite (= λ1811 3) λ1862 λ1867)))))))⟧) ∧
(⟦(= λ1869 (SRC2_OF λ1785))⟧) ∧
(⟦(= λ1870 (ite λ35 (ite (= λ1869 0) 0 (ite (= λ1869 λ1799) 2 (ite (= λ1869 λ1806) 1 (ite (= λ1869 λ1808) 4 (ite (= λ1869 λ1810) 3 5))))) λ1766))⟧) ∧
(⟦(= λ1871 (= λ1870 4))⟧) ∧
(⟦(= λ1872 (ite λ35 (select λ1866 λ1869) λ1768))⟧) ∧
(⟦(= λ1873 (ite (= λ1870 0) 0 (ite (= λ1870 2) λ1833 (ite (= λ1870 1) λ1844 (ite (ite λ1871 λ1848 false) λ1858 (ite λ1871 λ1860 (ite (= λ1870 3) λ1862 λ1872)))))))⟧) ∧
(⟦(= λ1874 (ite λ1130 λ1771 (ite λ1775 λ1771 (ite (ite λ1776 false true) (ite (ite λ1775 false true) (ite (= λ1787 12) true (ite (= λ1787 14) true (ite (= λ1787 13) true (ite (= λ1787 15) (BRANCH_CONDITION λ1868 λ1873) false)))) false) false))))⟧) ∧
(⟦(= λ1875 (ite λ1131 λ36 false))⟧) ∧
(⟦(= λ1876 (ite λ34 true λ1773))⟧) ∧
(⟦(= λ1877 (ite λ1875 λ1876 λ1774))⟧) ∧
(⟦(= λ1878 (ite λ36 λ1877 λ1775))⟧) ∧
(⟦(= λ1879 (ite λ36 λ1771 λ1776))⟧) ∧
(⟦(= λ1880 (ite λ1876 true λ1133))⟧) ∧
(⟦(= λ1881 (ite λ30 λ1469 λ1778))⟧) ∧
(⟦(= λ1882 (ite λ1459 λ1881 λ1779))⟧) ∧
(⟦(= λ1883 (ite λ1474 λ1555 (plus (OFFSET_OF λ1471) (plus 4 λ1882))))⟧) ∧
(⟦(= λ1884 (ite λ1141 (ite λ1564 λ1782 (ite λ1457 (plus 4 (plus 4 λ1780)) (plus 4 (plus 4 λ1781)))) λ1781))⟧) ∧
(⟦(= λ1885 (ite λ1561 λ1883 λ1884))⟧) ∧
(⟦(= λ1886 (ite λ1138 (ite λ1668 λ1783 λ1885) λ1783))⟧) ∧
(⟦(= λ1887 (ite λ34 (select IMEM_INIT λ1886) λ1784))⟧) ∧
(⟦(= λ1888 (ite λ1880 λ1785 λ1887))⟧) ∧
(⟦(= λ1889 (OPCODE_OF λ1888))⟧) ∧
(⟦(= λ1890 (ite λ36 λ1889 λ1787))⟧) ∧
(⟦(= λ1891 (SRC1_OF λ1888))⟧) ∧
(⟦(= λ1892 (ite λ32 true λ1789))⟧) ∧
(⟦(= λ1893 (ite λ1667 λ1892 λ1790))⟧) ∧
(⟦(= λ1894 (ite λ34 λ1893 λ1791))⟧) ∧
(⟦(= λ1895 (ite λ32 (select IMEM_INIT λ1732) λ1792))⟧) ∧
(⟦(= λ1896 (ite λ1672 λ1793 λ1895))⟧) ∧
(⟦(= λ1897 (OPCODE_OF λ1896))⟧) ∧
(⟦(= λ1898 (= λ1897 16))⟧) ∧
(⟦(= λ1899 (= λ1897 10))⟧) ∧
(⟦(= λ1900 (= λ1897 17))⟧) ∧
(⟦(= λ1901 (ite λ34 (ite λ1893 0 (ite (ite (ite λ1898 false (ite λ1899 true λ1900)) true λ1898) (DEST_OF λ1896) 0)) λ1798))⟧) ∧
(⟦(= λ1902 (ite λ1133 λ1799 (ite λ1894 0 λ1901)))⟧) ∧
(⟦(= λ1903 (ite λ32 true λ1800))⟧) ∧
(⟦(= λ1904 (ite λ1667 λ1903 λ1801))⟧) ∧
(⟦(= λ1905 (= λ1681 16))⟧) ∧
(⟦(= λ1906 (= λ1681 17))⟧) ∧
(⟦(= λ1907 (= λ1681 14))⟧) ∧
(⟦(= λ1908 (ite λ34 (ite λ1904 0 (ite (ite λ1905 false (ite λ1906 false (ite λ1907 (ite λ1562 false true) false))) 31 (ite (ite (ite λ1905 false λ1906) true λ1905) (DEST_OF λ1680) 0))) λ1805))⟧) ∧
(⟦(= λ1909 (ite λ1133 λ1806 λ1908))⟧) ∧
(⟦(= λ1910 (ite λ34 λ1695 λ1807))⟧) ∧
(⟦(= λ1911 (ite λ1133 λ1808 λ1910))⟧) ∧
(⟦(= λ1912 (ite λ34 λ1702 λ1809))⟧) ∧
(⟦(= λ1913 (ite λ1133 λ1810 λ1912))⟧) ∧
(⟦(= λ1914 (ite λ36 (ite (= λ1891 0) 0 (ite (= λ1902 λ1891) 2 (ite (= λ1909 λ1891) 1 (ite (= λ1911 λ1891) 4 (ite (= λ1913 λ1891) 3 5))))) λ1811))⟧) ∧
(⟦(= λ1915 (ite λ1893 false true))⟧) ∧
(⟦(= λ1916 (ite λ34 (ite λ1899 λ1915 false) λ1813))⟧) ∧
(⟦(= λ1917 (ite λ1133 λ1814 λ1916))⟧) ∧
(⟦(= λ1918 (= λ1897 11))⟧) ∧
(⟦(= λ1919 (ite λ34 (ite λ1918 λ1915 false) λ1816))⟧) ∧
(⟦(= λ1920 (ite λ1133 λ1817 λ1919))⟧) ∧
(⟦(= λ1921 (SRC1_OF λ1896))⟧) ∧
(⟦(= λ1922 (ite λ34 (ite (= λ1921 0) 0 (ite (= λ1921 λ1695) 2 (ite (= λ1921 λ1702) 1 (ite (= λ1921 λ1704) 4 (ite (= λ1921 λ1706) 3 5))))) λ1819))⟧) ∧
(⟦(= λ1923 (= λ1922 4))⟧) ∧
(⟦(= λ1924 (ite λ34 (select λ1762 λ1921) λ1821))⟧) ∧
(⟦(= λ1925 (ite λ1133 λ1822 (ite (= λ1922 0) 0 (ite (= λ1922 2) λ1729 (ite (= λ1922 1) λ1740 (ite (ite λ1923 λ1744 false) λ1754 (ite λ1923 λ1756 (ite (= λ1922 3) λ1758 λ1924))))))))⟧) ∧
(⟦(= λ1926 (ite λ34 (SHORT_IMMED_OF λ1896) λ1823))⟧) ∧
(⟦(= λ1927 (SRC2_OF λ1896))⟧) ∧
(⟦(= λ1928 (ite λ34 (ite (= λ1927 0) 0 (ite (= λ1927 λ1695) 2 (ite (= λ1927 λ1702) 1 (ite (= λ1927 λ1704) 4 (ite (= λ1927 λ1706) 3 5))))) λ1825))⟧) ∧
(⟦(= λ1929 (= λ1928 4))⟧) ∧
(⟦(= λ1930 (ite λ34 (select λ1762 λ1927) λ1827))⟧) ∧
(⟦(= λ1931 (ite (= λ1928 0) 0 (ite (= λ1928 2) λ1729 (ite (= λ1928 1) λ1740 (ite (ite λ1929 λ1744 false) λ1754 (ite λ1929 λ1756 (ite (= λ1928 3) λ1758 λ1930)))))))⟧) ∧
(⟦(= λ1932 (ite λ1133 λ1829 (ite (ite λ34 (ite λ1900 true (ite λ1899 true λ1918)) NO_VALUE34) λ1926 λ1931)))⟧) ∧
(⟦(= λ1933 (ite λ34 λ1897 λ1830))⟧) ∧
(⟦(= λ1934 (ite λ1133 λ1831 λ1933))⟧) ∧
(⟦(= λ1935 (ite (ite λ1917 true λ1920) (plus λ1925 λ1932) (ALU (ALU_OP_OF λ1934) λ1925 λ1932)))⟧) ∧
(⟦(= λ1936 (ite λ36 λ1935 λ1833))⟧) ∧
(⟦(= λ1937 (ite λ34 λ1907 λ1834))⟧) ∧
(⟦(= λ1938 (ite λ1133 λ1835 λ1937))⟧) ∧
(⟦(= λ1939 (plus 4 λ1886))⟧) ∧
(⟦(= λ1940 (ite λ34 (plus 4 λ1939) λ1837))⟧) ∧
(⟦(= λ1941 (ite λ1875 λ1940 λ1838))⟧) ∧
(⟦(= λ1942 (ite λ1133 λ1839 λ1682))⟧) ∧
(⟦(= λ1943 (ite λ1133 λ1840 λ1764))⟧) ∧
(⟦(= λ1944 (ite λ34 λ1906 λ1841))⟧) ∧
(⟦(= λ1945 (ite λ34 (SHORT_IMMED_OF λ1680) λ1842))⟧) ∧
(⟦(= λ1946 (ite λ1133 λ1843 (ite λ1944 λ1945 λ1769)))⟧) ∧
(⟦(= λ1947 (ite λ36 (ite λ1938 λ1941 (ALU (ALU_OP_OF λ1942) λ1943 λ1946)) λ1844))⟧) ∧
(⟦(= λ1948 (= λ1914 4))⟧) ∧
(⟦(= λ1949 (ite λ34 λ1710 λ1846))⟧) ∧
(⟦(= λ1950 (ite λ1132 λ1949 λ1847))⟧) ∧
(⟦(= λ1951 (ite λ36 λ1950 λ1848))⟧) ∧
(⟦(= λ1952 (ite λ34 λ1713 λ1849))⟧) ∧
(⟦(= λ1953 (ite λ34 λ1728 λ1850))⟧) ∧
(⟦(= λ1954 (ite λ1139 λ1851 λ1724))⟧) ∧
(⟦(= λ1955 (ite λ34 λ1954 λ1852))⟧) ∧
(⟦(= λ1956 (ite (ite λ36 (ite λ1952 λ1131 false) false) (store λ1853 λ1953 λ1955) λ1853))⟧) ∧
(⟦(= λ1957 (ite λ34 λ1728 λ1854))⟧) ∧
(⟦(= λ1958 (ite λ1138 λ1750 λ1855))⟧) ∧
(⟦(= λ1959 (ite λ34 λ1958 λ1856))⟧) ∧
(⟦(= λ1960 (ite λ36 (select λ1956 (ite (ite λ1949 λ1131 false) λ1957 λ1959)) λ1857))⟧) ∧
(⟦(= λ1961 (ite (ite λ1950 λ36 false) (ite λ1950 λ1960 NO_VALUE35) λ1858))⟧) ∧
(⟦(= λ1962 (ite λ1133 λ1859 λ1729))⟧) ∧
(⟦(= λ1963 (ite λ36 λ1962 λ1860))⟧) ∧
(⟦(= λ1964 (ite λ1133 λ1861 λ1740))⟧) ∧
(⟦(= λ1965 (ite λ36 λ1964 λ1862))⟧) ∧
(⟦(= λ1966 (ite λ34 λ1704 λ1863))⟧) ∧
(⟦(= λ1967 (ite λ34 λ1706 λ1864))⟧) ∧
(⟦(= λ1968 (ite (ite (ite (= λ1967 0) false true) λ1132 false) (store λ1866 λ1967 λ1758) λ1866))⟧) ∧
(⟦(= λ1969 (ite (ite (ite (= λ1966 0) false true) λ1132 false) (store λ1968 λ1966 (ite λ1744 λ1754 λ1756)) λ1968))⟧) ∧
(⟦(= λ1970 (ite λ36 (select λ1969 λ1891) λ1867))⟧) ∧
(⟦(= λ1971 (ite (= λ1914 0) 0 (ite (= λ1914 2) λ1936 (ite (= λ1914 1) λ1947 (ite (ite λ1948 λ1951 false) λ1961 (ite λ1948 λ1963 (ite (= λ1914 3) λ1965 λ1970)))))))⟧) ∧
(⟦(= λ1972 (SRC2_OF λ1888))⟧) ∧
(⟦(= λ1973 (ite λ36 (ite (= λ1972 0) 0 (ite (= λ1972 λ1902) 2 (ite (= λ1972 λ1909) 1 (ite (= λ1972 λ1911) 4 (ite (= λ1972 λ1913) 3 5))))) λ1870))⟧) ∧
(⟦(= λ1974 (= λ1973 4))⟧) ∧
(⟦(= λ1975 (ite λ36 (select λ1969 λ1972) λ1872))⟧) ∧
(⟦(= λ1976 (ite (= λ1973 0) 0 (ite (= λ1973 2) λ1936 (ite (= λ1973 1) λ1947 (ite (ite λ1974 λ1951 false) λ1961 (ite λ1974 λ1963 (ite (= λ1973 3) λ1965 λ1975)))))))⟧) ∧
(⟦(= λ1977 (ite λ1127 λ1874 (ite λ1878 λ1874 (ite (ite λ1879 false true) (ite (ite λ1878 false true) (ite (= λ1890 12) true (ite (= λ1890 14) true (ite (= λ1890 13) true (ite (= λ1890 15) (BRANCH_CONDITION λ1971 λ1976) false)))) false) false))))⟧) ∧
(⟦(= λ1978 (ite λ1128 λ37 false))⟧) ∧
(⟦(= λ1979 (ite λ35 true λ1876))⟧) ∧
(⟦(= λ1980 (ite λ1978 λ1979 λ1877))⟧) ∧
(⟦(= λ1981 (ite λ37 λ1980 λ1878))⟧) ∧
(⟦(= λ1982 (ite λ37 λ1874 λ1879))⟧) ∧
(⟦(= λ1983 (ite λ31 λ1573 λ1881))⟧) ∧
(⟦(= λ1984 (ite λ1563 λ1983 λ1882))⟧) ∧
(⟦(= λ1985 (ite λ1578 λ1659 (plus (OFFSET_OF λ1575) (plus 4 λ1984))))⟧) ∧
(⟦(= λ1986 (ite λ1138 (ite λ1668 λ1885 (ite λ1561 (plus 4 (plus 4 λ1883)) (plus 4 (plus 4 λ1884)))) λ1884))⟧) ∧
(⟦(= λ1987 (ite λ1665 λ1985 λ1986))⟧) ∧
(⟦(= λ1988 (ite λ1135 (ite λ1773 λ1886 λ1987) λ1886))⟧) ∧
(⟦(= λ1989 (ite λ35 (select IMEM_INIT λ1988) λ1887))⟧) ∧
(⟦(= λ1990 (ite (ite λ1979 true λ1130) λ1888 λ1989))⟧) ∧
(⟦(= λ1991 (ite λ37 (OPCODE_OF λ1990) λ1890))⟧) ∧
(⟦(= λ1992 (SRC1_OF λ1990))⟧) ∧
(⟦(= λ1993 (ite λ33 true λ1892))⟧) ∧
(⟦(= λ1994 (ite λ1772 λ1993 λ1893))⟧) ∧
(⟦(= λ1995 (ite λ35 λ1994 λ1894))⟧) ∧
(⟦(= λ1996 (ite λ33 (select IMEM_INIT λ1836) λ1895))⟧) ∧
(⟦(= λ1997 (ite λ1777 λ1896 λ1996))⟧) ∧
(⟦(= λ1998 (OPCODE_OF λ1997))⟧) ∧
(⟦(= λ1999 (= λ1998 16))⟧) ∧
(⟦(= λ2000 (= λ1998 10))⟧) ∧
(⟦(= λ2001 (= λ1998 17))⟧) ∧
(⟦(= λ2002 (ite λ35 (ite λ1994 0 (ite (ite (ite λ1999 false (ite λ2000 true λ2001)) true λ1999) (DEST_OF λ1997) 0)) λ1901))⟧) ∧
(⟦(= λ2003 (ite λ1130 λ1902 (ite λ1995 0 λ2002)))⟧) ∧
(⟦(= λ2004 (ite λ33 true λ1903))⟧) ∧
(⟦(= λ2005 (ite λ1772 λ2004 λ1904))⟧) ∧
(⟦(= λ2006 (= λ1786 16))⟧) ∧
(⟦(= λ2007 (= λ1786 17))⟧) ∧
(⟦(= λ2008 (= λ1786 14))⟧) ∧
(⟦(= λ2009 (ite λ35 (ite λ2005 0 (ite (ite λ2006 false (ite λ2007 false (ite λ2008 (ite λ1666 false true) false))) 31 (ite (ite (ite λ2006 false λ2007) true λ2006) (DEST_OF λ1785) 0))) λ1908))⟧) ∧
(⟦(= λ2010 (ite λ1130 λ1909 λ2009))⟧) ∧
(⟦(= λ2011 (ite λ35 λ1799 λ1910))⟧) ∧
(⟦(= λ2012 (ite λ1130 λ1911 λ2011))⟧) ∧
(⟦(= λ2013 (ite λ35 λ1806 λ1912))⟧) ∧
(⟦(= λ2014 (ite λ1130 λ1913 λ2013))⟧) ∧
(⟦(= λ2015 (ite λ37 (ite (= λ1992 0) 0 (ite (= λ2003 λ1992) 2 (ite (= λ2010 λ1992) 1 (ite (= λ2012 λ1992) 4 (ite (= λ2014 λ1992) 3 5))))) λ1914))⟧) ∧
(⟦(= λ2016 (ite λ1994 false true))⟧) ∧
(⟦(= λ2017 (ite λ35 (ite λ2000 λ2016 false) λ1916))⟧) ∧
(⟦(= λ2018 (ite λ1130 λ1917 λ2017))⟧) ∧
(⟦(= λ2019 (= λ1998 11))⟧) ∧
(⟦(= λ2020 (ite λ35 (ite λ2019 λ2016 false) λ1919))⟧) ∧
(⟦(= λ2021 (ite λ1130 λ1920 λ2020))⟧) ∧
(⟦(= λ2022 (SRC1_OF λ1997))⟧) ∧
(⟦(= λ2023 (ite λ35 (ite (= λ2022 0) 0 (ite (= λ2022 λ1799) 2 (ite (= λ2022 λ1806) 1 (ite (= λ2022 λ1808) 4 (ite (= λ2022 λ1810) 3 5))))) λ1922))⟧) ∧
(⟦(= λ2024 (= λ2023 4))⟧) ∧
(⟦(= λ2025 (ite λ35 (select λ1866 λ2022) λ1924))⟧) ∧
(⟦(= λ2026 (ite λ1130 λ1925 (ite (= λ2023 0) 0 (ite (= λ2023 2) λ1833 (ite (= λ2023 1) λ1844 (ite (ite λ2024 λ1848 false) λ1858 (ite λ2024 λ1860 (ite (= λ2023 3) λ1862 λ2025))))))))⟧) ∧
(⟦(= λ2027 (ite λ35 (SHORT_IMMED_OF λ1997) λ1926))⟧) ∧
(⟦(= λ2028 (SRC2_OF λ1997))⟧) ∧
(⟦(= λ2029 (ite λ35 (ite (= λ2028 0) 0 (ite (= λ2028 λ1799) 2 (ite (= λ2028 λ1806) 1 (ite (= λ2028 λ1808) 4 (ite (= λ2028 λ1810) 3 5))))) λ1928))⟧) ∧
(⟦(= λ2030 (= λ2029 4))⟧) ∧
(⟦(= λ2031 (ite λ35 (select λ1866 λ2028) λ1930))⟧) ∧
(⟦(= λ2032 (ite λ1130 λ1932 (ite (ite λ35 (ite λ2001 true (ite λ2000 true λ2019)) NO_VALUE36) λ2027 (ite (= λ2029 0) 0 (ite (= λ2029 2) λ1833 (ite (= λ2029 1) λ1844 (ite (ite λ2030 λ1848 false) λ1858 (ite λ2030 λ1860 (ite (= λ2029 3) λ1862 λ2031)))))))))⟧) ∧
(⟦(= λ2033 (ite λ35 λ1998 λ1933))⟧) ∧
(⟦(= λ2034 (ite λ1130 λ1934 λ2033))⟧) ∧
(⟦(= λ2035 (ite λ37 (ite (ite λ2018 true λ2021) (plus λ2026 λ2032) (ALU (ALU_OP_OF λ2034) λ2026 λ2032)) λ1936))⟧) ∧
(⟦(= λ2036 (ite λ35 λ2008 λ1937))⟧) ∧
(⟦(= λ2037 (ite λ1130 λ1938 λ2036))⟧) ∧
(⟦(= λ2038 (ite λ35 (plus 4 (plus 4 λ1988)) λ1940))⟧) ∧
(⟦(= λ2039 (ite λ1978 λ2038 λ1941))⟧) ∧
(⟦(= λ2040 (ite λ1130 λ1942 λ1787))⟧) ∧
(⟦(= λ2041 (ite λ1130 λ1943 λ1868))⟧) ∧
(⟦(= λ2042 (ite λ35 λ2007 λ1944))⟧) ∧
(⟦(= λ2043 (ite λ35 (SHORT_IMMED_OF λ1785) λ1945))⟧) ∧
(⟦(= λ2044 (ite λ1130 λ1946 (ite λ2042 λ2043 λ1873)))⟧) ∧
(⟦(= λ2045 (ite λ37 (ite λ2037 λ2039 (ALU (ALU_OP_OF λ2040) λ2041 λ2044)) λ1947))⟧) ∧
(⟦(= λ2046 (= λ2015 4))⟧) ∧
(⟦(= λ2047 (ite λ35 λ1814 λ1949))⟧) ∧
(⟦(= λ2048 (ite λ1129 λ2047 λ1950))⟧) ∧
(⟦(= λ2049 (ite λ37 λ2048 λ1951))⟧) ∧
(⟦(= λ2050 (ite λ35 λ1817 λ1952))⟧) ∧
(⟦(= λ2051 (ite λ35 λ1832 λ1953))⟧) ∧
(⟦(= λ2052 (ite λ1136 λ1954 λ1828))⟧) ∧
(⟦(= λ2053 (ite λ35 λ2052 λ1955))⟧) ∧
(⟦(= λ2054 (ite (ite λ37 (ite λ2050 λ1128 false) false) (store λ1956 λ2051 λ2053) λ1956))⟧) ∧
(⟦(= λ2055 (ite λ35 λ1832 λ1957))⟧) ∧
(⟦(= λ2056 (ite λ1135 λ1854 λ1958))⟧) ∧
(⟦(= λ2057 (ite λ35 λ2056 λ1959))⟧) ∧
(⟦(= λ2058 (ite λ37 (select λ2054 (ite (ite λ2047 λ1128 false) λ2055 λ2057)) λ1960))⟧) ∧
(⟦(= λ2059 (ite (ite λ2048 λ37 false) (ite λ2048 λ2058 NO_VALUE37) λ1961))⟧) ∧
(⟦(= λ2060 (ite λ1130 λ1962 λ1833))⟧) ∧
(⟦(= λ2061 (ite λ37 λ2060 λ1963))⟧) ∧
(⟦(= λ2062 (ite λ1130 λ1964 λ1844))⟧) ∧
(⟦(= λ2063 (ite λ37 λ2062 λ1965))⟧) ∧
(⟦(= λ2064 (ite λ35 λ1808 λ1966))⟧) ∧
(⟦(= λ2065 (ite λ35 λ1810 λ1967))⟧) ∧
(⟦(= λ2066 (ite (ite (ite (= λ2065 0) false true) λ1129 false) (store λ1969 λ2065 λ1862) λ1969))⟧) ∧
(⟦(= λ2067 (ite (ite (ite (= λ2064 0) false true) λ1129 false) (store λ2066 λ2064 (ite λ1848 λ1858 λ1860)) λ2066))⟧) ∧
(⟦(= λ2068 (ite λ37 (select λ2067 λ1992) λ1970))⟧) ∧
(⟦(= λ2069 (SRC2_OF λ1990))⟧) ∧
(⟦(= λ2070 (ite λ37 (ite (= λ2069 0) 0 (ite (= λ2069 λ2003) 2 (ite (= λ2069 λ2010) 1 (ite (= λ2069 λ2012) 4 (ite (= λ2069 λ2014) 3 5))))) λ1973))⟧) ∧
(⟦(= λ2071 (= λ2070 4))⟧) ∧
(⟦(= λ2072 (ite λ37 (select λ2067 λ2069) λ1975))⟧) ∧
(⟦(= λ2073 (ite (ite (ite λ1113 (ite λ1124 false true) false) false true) λ1977 (ite λ1981 λ1977 (ite (ite λ1982 false true) (ite (ite λ1981 false true) (ite (= λ1991 12) true (ite (= λ1991 14) true (ite (= λ1991 13) true (ite (= λ1991 15) (BRANCH_CONDITION (ite (= λ2015 0) 0 (ite (= λ2015 2) λ2035 (ite (= λ2015 1) λ2045 (ite (ite λ2046 λ2049 false) λ2059 (ite λ2046 λ2061 (ite (= λ2015 3) λ2063 λ2068)))))) (ite (= λ2070 0) 0 (ite (= λ2070 2) λ2035 (ite (= λ2070 1) λ2045 (ite (ite λ2071 λ2049 false) λ2059 (ite λ2071 λ2061 (ite (= λ2070 3) λ2063 λ2072))))))) false)))) false) false))))⟧) ∧
(⟦(= λ2074 (ite λ1125 λ38 false))⟧) ∧
(⟦(= λ2075 (ite λ36 true λ1979))⟧) ∧
(⟦(= λ2076 (ite λ38 (ite λ2074 λ2075 λ1980) λ1981))⟧) ∧
(⟦(= λ2077 (ite λ1132 (ite λ1876 λ1988 (ite λ1770 (ite λ1683 λ1764 (plus (OFFSET_OF λ1680) (plus 4 (ite λ1667 (ite λ32 λ1678 λ1983) λ1984)))) (ite λ1135 (ite λ1773 λ1987 (ite λ1665 (plus 4 (plus 4 λ1985)) (plus 4 (plus 4 λ1986)))) λ1986))) λ1988))⟧) ∧
(⟦(= λ2078 (ite (ite λ2075 true λ1127) λ1990 (ite λ36 (select IMEM_INIT λ2077) λ1989)))⟧) ∧
(⟦(= λ2079 (ite λ38 (OPCODE_OF λ2078) λ1991))⟧) ∧
(⟦(= λ2080 (SRC1_OF λ2078))⟧) ∧
(⟦(= λ2081 (ite λ1875 (ite λ34 true λ1993) λ1994))⟧) ∧
(⟦(= λ2082 (ite λ1880 λ1997 (ite λ34 (select IMEM_INIT λ1939) λ1996)))⟧) ∧
(⟦(= λ2083 (OPCODE_OF λ2082))⟧) ∧
(⟦(= λ2084 (= λ2083 16))⟧) ∧
(⟦(= λ2085 (= λ2083 10))⟧) ∧
(⟦(= λ2086 (= λ2083 17))⟧) ∧
(⟦(= λ2087 (ite λ1127 λ2003 (ite (ite λ36 λ2081 λ1995) 0 (ite λ36 (ite λ2081 0 (ite (ite (ite λ2084 false (ite λ2085 true λ2086)) true λ2084) (DEST_OF λ2082) 0)) λ2002))))⟧) ∧
(⟦(= λ2088 (= λ1889 16))⟧) ∧
(⟦(= λ2089 (= λ1889 17))⟧) ∧
(⟦(= λ2090 (= λ1889 14))⟧) ∧
(⟦(= λ2091 (ite λ1127 λ2010 (ite λ36 (ite (ite λ1875 (ite λ34 true λ2004) λ2005) 0 (ite (ite λ2088 false (ite λ2089 false (ite λ2090 (ite λ1771 false true) false))) 31 (ite (ite (ite λ2088 false λ2089) true λ2088) (DEST_OF λ1888) 0))) λ2009)))⟧) ∧
(⟦(= λ2092 (ite λ1127 λ2012 (ite λ36 λ1902 λ2011)))⟧) ∧
(⟦(= λ2093 (ite λ1127 λ2014 (ite λ36 λ1909 λ2013)))⟧) ∧
(⟦(= λ2094 (ite λ38 (ite (= λ2080 0) 0 (ite (= λ2087 λ2080) 2 (ite (= λ2091 λ2080) 1 (ite (= λ2092 λ2080) 4 (ite (= λ2093 λ2080) 3 5))))) λ2015))⟧) ∧
(⟦(= λ2095 (ite λ2081 false true))⟧) ∧
(⟦(= λ2096 (= λ2083 11))⟧) ∧
(⟦(= λ2097 (SRC1_OF λ2082))⟧) ∧
(⟦(= λ2098 (ite λ36 (ite (= λ2097 0) 0 (ite (= λ2097 λ1902) 2 (ite (= λ2097 λ1909) 1 (ite (= λ2097 λ1911) 4 (ite (= λ2097 λ1913) 3 5))))) λ2023))⟧) ∧
(⟦(= λ2099 (= λ2098 4))⟧) ∧
(⟦(= λ2100 (ite λ1127 λ2026 (ite (= λ2098 0) 0 (ite (= λ2098 2) λ1936 (ite (= λ2098 1) λ1947 (ite (ite λ2099 λ1951 false) λ1961 (ite λ2099 λ1963 (ite (= λ2098 3) λ1965 (ite λ36 (select λ1969 λ2097) λ2025)))))))))⟧) ∧
(⟦(= λ2101 (SRC2_OF λ2082))⟧) ∧
(⟦(= λ2102 (ite λ36 (ite (= λ2101 0) 0 (ite (= λ2101 λ1902) 2 (ite (= λ2101 λ1909) 1 (ite (= λ2101 λ1911) 4 (ite (= λ2101 λ1913) 3 5))))) λ2029))⟧) ∧
(⟦(= λ2103 (= λ2102 4))⟧) ∧
(⟦(= λ2104 (ite λ1127 λ2032 (ite (ite λ36 (ite λ2086 true (ite λ2085 true λ2096)) NO_VALUE38) (ite λ36 (SHORT_IMMED_OF λ2082) λ2027) (ite (= λ2102 0) 0 (ite (= λ2102 2) λ1936 (ite (= λ2102 1) λ1947 (ite (ite λ2103 λ1951 false) λ1961 (ite λ2103 λ1963 (ite (= λ2102 3) λ1965 (ite λ36 (select λ1969 λ2101) λ2031))))))))))⟧) ∧
(⟦(= λ2105 (ite λ38 (ite (ite (ite λ1127 λ2018 (ite λ36 (ite λ2085 λ2095 false) λ2017)) true (ite λ1127 λ2021 (ite λ36 (ite λ2096 λ2095 false) λ2020))) (plus λ2100 λ2104) (ALU (ALU_OP_OF (ite λ1127 λ2034 (ite λ36 λ2083 λ2033))) λ2100 λ2104)) λ2035))⟧) ∧
(⟦(= λ2106 (ite λ38 (ite (ite λ1127 λ2037 (ite λ36 λ2090 λ2036)) (ite λ2074 (ite λ36 (plus 4 (plus 4 λ2077)) λ2038) λ2039) (ALU (ALU_OP_OF (ite λ1127 λ2040 λ1890)) (ite λ1127 λ2041 λ1971) (ite λ1127 λ2044 (ite (ite λ36 λ2089 λ2042) (ite λ36 (SHORT_IMMED_OF λ1888) λ2043) λ1976)))) λ2045))⟧) ∧
(⟦(= λ2107 (= λ2094 4))⟧) ∧
(⟦(= λ2108 (ite λ36 λ1917 λ2047))⟧) ∧
(⟦(= λ2109 (ite λ1126 λ2108 λ2048))⟧) ∧
(⟦(= λ2110 (ite λ38 λ2109 λ2049))⟧) ∧
(⟦(= λ2111 (ite (ite λ2109 λ38 false) (ite λ2109 (ite λ38 (select (ite (ite λ38 (ite (ite λ36 λ1920 λ2050) λ1125 false) false) (store λ2054 (ite λ36 λ1935 λ2051) (ite λ36 (ite λ1133 λ2052 λ1931) λ2053)) λ2054) (ite (ite λ2108 λ1125 false) (ite λ36 λ1935 λ2055) (ite λ36 (ite λ1132 λ1957 λ2056) λ2057))) λ2058) NO_VALUE39) λ2059))⟧) ∧
(⟦(= λ2112 (ite λ38 (ite λ1127 λ2060 λ1936) λ2061))⟧) ∧
(⟦(= λ2113 (ite λ38 (ite λ1127 λ2062 λ1947) λ2063))⟧) ∧
(⟦(= λ2114 (ite λ36 λ1911 λ2064))⟧) ∧
(⟦(= λ2115 (ite λ36 λ1913 λ2065))⟧) ∧
(⟦(= λ2116 (ite (ite (ite (= λ2115 0) false true) λ1126 false) (store λ2067 λ2115 λ1965) λ2067))⟧) ∧
(⟦(= λ2117 (ite (ite (ite (= λ2114 0) false true) λ1126 false) (store λ2116 λ2114 (ite λ1951 λ1961 λ1963)) λ2116))⟧) ∧
(⟦(= λ2118 (SRC2_OF λ2078))⟧) ∧
(⟦(= λ2119 (ite λ38 (ite (= λ2118 0) 0 (ite (= λ2118 λ2087) 2 (ite (= λ2118 λ2091) 1 (ite (= λ2118 λ2092) 4 (ite (= λ2118 λ2093) 3 5))))) λ2070))⟧) ∧
(⟦(= λ2120 (= λ2119 4))⟧) ∧
(⟦INSTRISLOAD_S2E_INIT⟧ ∨ τ1) ∧
(¬⟦INSTRISLOAD_S2E_INIT⟧ ∨ ⟦INSTRISSTORE_S2E_INIT⟧ ∨ τ1) ∧
(¬⟦INSTRISLOAD_S2E_INIT⟧ ∨ ¬⟦INSTRISSTORE_S2E_INIT⟧ ∨ ¬τ1) ∧
(¬⟦INSTRISSTORE_S2E_INIT⟧ ∨ ¬⟦(= BDEST_S2E_INIT 0)⟧ ∨ τ2) ∧
(¬⟦INSTRISSTORE_S2E_INIT⟧ ∨ ⟦(= BDEST_S2E_INIT 0)⟧ ∨ ¬τ2) ∧
(⟦INSTRISSTORE_S2E_INIT⟧ ∨ τ2) ∧
(¬⟦(= ADEST_S2E_INIT 31)⟧ ∨ τ3) ∧
(⟦(= ADEST_S2E_INIT 31)⟧ ∨ ¬⟦(= ADEST_S2E_INIT 0)⟧ ∨ τ3) ∧
(⟦(= ADEST_S2E_INIT 31)⟧ ∨ ⟦(= ADEST_S2E_INIT 0)⟧ ∨ ¬τ3) ∧
(¬⟦PCDRVRESULT_S2E_INIT⟧ ∨ ¬τ3 ∨ τ4) ∧
(¬⟦PCDRVRESULT_S2E_INIT⟧ ∨ τ3 ∨ ¬τ4) ∧
(⟦PCDRVRESULT_S2E_INIT⟧ ∨ τ4) ∧
(¬⟦INSTRISLOAD_S2E_INIT⟧ ∨ ¬⟦λ1⟧ ∨ τ5) ∧
(¬⟦INSTRISLOAD_S2E_INIT⟧ ∨ ⟦λ1⟧ ∨ ¬τ5) ∧
(⟦INSTRISLOAD_S2E_INIT⟧ ∨ ⟦λ1⟧ ∨ τ5) ∧
(⟦INSTRISLOAD_S2E_INIT⟧ ∨ ¬⟦λ1⟧ ∨ ¬τ5) ∧
(¬⟦INSTRISSTORE_S2E_INIT⟧ ∨ ¬⟦λ2⟧ ∨ τ6) ∧
(¬⟦INSTRISSTORE_S2E_INIT⟧ ∨ ⟦λ2⟧ ∨ ¬τ6) ∧
(⟦INSTRISSTORE_S2E_INIT⟧ ∨ ⟦λ2⟧ ∨ τ6) ∧
(⟦INSTRISSTORE_S2E_INIT⟧ ∨ ¬⟦λ2⟧ ∨ ¬τ6) ∧
(¬⟦INSTRISLOAD_S2M_INIT⟧ ∨ ¬⟦(= (select DMEM_INIT STOREADDR_S2M_INIT) CACHEDOUT_S2_INIT)⟧ ∨ τ7) ∧
(¬⟦INSTRISLOAD_S2M_INIT⟧ ∨ ⟦(= (select DMEM_INIT STOREADDR_S2M_INIT) CACHEDOUT_S2_INIT)⟧ ∨ ¬τ7) ∧
(⟦INSTRISLOAD_S2M_INIT⟧ ∨ τ7) ∧
(⟦ABUBBLE_S2R_INIT⟧ ∨ ¬⟦λ5⟧ ∨ τ8) ∧
(⟦ABUBBLE_S2R_INIT⟧ ∨ ⟦λ5⟧ ∨ ¬τ8) ∧
(¬⟦ABUBBLE_S2R_INIT⟧ ∨ ¬τ8) ∧
(¬⟦(= λ4 PC_PLUS_S2I_INIT)⟧ ∨ ¬τ8 ∨ τ9) ∧
(¬⟦(= λ4 PC_PLUS_S2I_INIT)⟧ ∨ τ8 ∨ ¬τ9) ∧
(⟦(= λ4 PC_PLUS_S2I_INIT)⟧ ∨ ¬τ9) ∧
(¬τ7 ∨ ¬τ9 ∨ τ10) ∧
(¬τ7 ∨ τ9 ∨ ¬τ10) ∧
(τ7 ∨ ¬τ10) ∧
(¬τ6 ∨ ¬τ10 ∨ τ11) ∧
(¬τ6 ∨ τ10 ∨ ¬τ11) ∧
(τ6 ∨ ¬τ11) ∧
(¬τ5 ∨ ¬τ11 ∨ τ12) ∧
(¬τ5 ∨ τ11 ∨ ¬τ12) ∧
(τ5 ∨ ¬τ12) ∧
(¬τ4 ∨ ¬τ12 ∨ τ13) ∧
(¬τ4 ∨ τ12 ∨ ¬τ13) ∧
(τ4 ∨ ¬τ13) ∧
(¬τ2 ∨ ¬τ13 ∨ τ14) ∧
(¬τ2 ∨ τ13 ∨ ¬τ14) ∧
(τ2 ∨ ¬τ14) ∧
(⟦STALL_S2R_INIT⟧ ∨ ¬τ14 ∨ τ15) ∧
(⟦STALL_S2R_INIT⟧ ∨ τ14 ∨ ¬τ15) ∧
(¬⟦STALL_S2R_INIT⟧ ∨ ¬τ15) ∧
(¬τ1 ∨ ¬τ15 ∨ τ16) ∧
(¬τ1 ∨ τ15 ∨ ¬τ16) ∧
(τ1 ∨ ¬τ16) ∧
(¬⟦CLOCK_INIT⟧ ∨ ¬τ16 ∨ τ17) ∧
(¬⟦CLOCK_INIT⟧ ∨ τ16 ∨ ¬τ17) ∧
(⟦CLOCK_INIT⟧ ∨ ¬τ17) ∧
(¬⟦INSTRISLOAD_S2E_INIT⟧ ∨ ¬⟦λ7⟧ ∨ τ18) ∧
(¬⟦INSTRISLOAD_S2E_INIT⟧ ∨ ⟦λ7⟧ ∨ ¬τ18) ∧
(⟦INSTRISLOAD_S2E_INIT⟧ ∨ ¬τ18) ∧
(¬⟦INSTRISLOAD_S2E_INIT⟧ ∨ ¬⟦λ9⟧ ∨ τ19) ∧
(¬⟦INSTRISLOAD_S2E_INIT⟧ ∨ ⟦λ9⟧ ∨ ¬τ19) ∧
(⟦INSTRISLOAD_S2E_INIT⟧ ∨ ¬τ19) ∧
(¬⟦INSTRISLOAD_S2E_INIT⟧ ∨ ¬⟦λ11⟧ ∨ τ20) ∧
(¬⟦INSTRISLOAD_S2E_INIT⟧ ∨ ⟦λ11⟧ ∨ ¬τ20) ∧
(⟦INSTRISLOAD_S2E_INIT⟧ ∨ ¬τ20) ∧
(¬⟦INSTRISLOAD_S2E_INIT⟧ ∨ ¬⟦λ13⟧ ∨ τ21) ∧
(¬⟦INSTRISLOAD_S2E_INIT⟧ ∨ ⟦λ13⟧ ∨ ¬τ21) ∧
(⟦INSTRISLOAD_S2E_INIT⟧ ∨ ¬τ21) ∧
(¬⟦λ21⟧ ∨ ¬⟦(= λ19 31)⟧ ∨ τ22) ∧
(¬⟦λ21⟧ ∨ ⟦(= λ19 31)⟧ ∨ ¬τ22) ∧
(⟦λ21⟧ ∨ ¬τ22) ∧
(¬⟦λ21⟧ ∨ ¬⟦(= λ20 31)⟧ ∨ τ23) ∧
(¬⟦λ21⟧ ∨ ⟦(= λ20 31)⟧ ∨ ¬τ23) ∧
(⟦λ21⟧ ∨ ¬τ23) ∧
(¬⟦λ23⟧ ∨ ¬⟦(= (SRC1_OF λ14) λ24)⟧ ∨ τ24) ∧
(¬⟦λ23⟧ ∨ ⟦(= (SRC1_OF λ14) λ24)⟧ ∨ ¬τ24) ∧
(⟦λ23⟧ ∨ ¬τ24) ∧
(¬⟦λ23⟧ ∨ ¬⟦(= (SRC2_OF λ14) λ24)⟧ ∨ τ25) ∧
(¬⟦λ23⟧ ∨ ⟦(= (SRC2_OF λ14) λ24)⟧ ∨ ¬τ25) ∧
(⟦λ23⟧ ∨ ¬τ25) ∧
(¬⟦λ23⟧ ∨ ¬⟦(= λ19 λ24)⟧ ∨ τ26) ∧
(¬⟦λ23⟧ ∨ ⟦(= λ19 λ24)⟧ ∨ ¬τ26) ∧
(⟦λ23⟧ ∨ ¬τ26) ∧
(¬⟦λ23⟧ ∨ ¬⟦(= λ20 λ24)⟧ ∨ τ27) ∧
(¬⟦λ23⟧ ∨ ⟦(= λ20 λ24)⟧ ∨ ¬τ27) ∧
(⟦λ23⟧ ∨ ¬τ27) ∧
(τ26 ∨ τ27 ∨ τ28) ∧
(τ26 ∨ ¬τ27 ∨ ¬τ28) ∧
(¬τ26 ∨ ¬τ28) ∧
(τ25 ∨ ¬τ28 ∨ τ29) ∧
(τ25 ∨ τ28 ∨ ¬τ29) ∧
(¬τ25 ∨ ¬τ29) ∧
(τ24 ∨ ¬τ29 ∨ τ30) ∧
(τ24 ∨ τ29 ∨ ¬τ30) ∧
(¬τ24 ∨ ¬τ30) ∧
(τ23 ∨ ¬τ30 ∨ τ31) ∧
(τ23 ∨ τ30 ∨ ¬τ31) ∧
(¬τ23 ∨ ¬τ31) ∧
(τ22 ∨ ¬τ31 ∨ τ32) ∧
(τ22 ∨ τ31 ∨ ¬τ32) ∧
(¬τ22 ∨ ¬τ32) ∧
(⟦(= (DEST_OF λ16) λ18)⟧ ∨ ¬τ32 ∨ τ33) ∧
(⟦(= (DEST_OF λ16) λ18)⟧ ∨ τ32 ∨ ¬τ33) ∧
(¬⟦(= (DEST_OF λ16) λ18)⟧ ∨ ¬τ33) ∧
(⟦(= λ20 λ18)⟧ ∨ ¬τ33 ∨ τ34) ∧
(⟦(= λ20 λ18)⟧ ∨ τ33 ∨ ¬τ34) ∧
(¬⟦(= λ20 λ18)⟧ ∨ ¬τ34) ∧
(⟦(= λ19 λ18)⟧ ∨ ¬τ34 ∨ τ35) ∧
(⟦(= λ19 λ18)⟧ ∨ τ34 ∨ ¬τ35) ∧
(¬⟦(= λ19 λ18)⟧ ∨ ¬τ35) ∧
(⟦(= λ17 15)⟧ ∨ ¬τ35 ∨ τ36) ∧
(⟦(= λ17 15)⟧ ∨ τ35 ∨ ¬τ36) ∧
(¬⟦(= λ17 15)⟧ ∨ ¬τ36) ∧
(⟦(= λ17 14)⟧ ∨ ¬τ36 ∨ τ37) ∧
(⟦(= λ17 14)⟧ ∨ τ36 ∨ ¬τ37) ∧
(¬⟦(= λ17 14)⟧ ∨ ¬τ37) ∧
(⟦(= λ17 13)⟧ ∨ ¬τ37 ∨ τ38) ∧
(⟦(= λ17 13)⟧ ∨ τ37 ∨ ¬τ38) ∧
(¬⟦(= λ17 13)⟧ ∨ ¬τ38) ∧
(⟦(= λ17 12)⟧ ∨ ¬τ38 ∨ τ39) ∧
(⟦(= λ17 12)⟧ ∨ τ38 ∨ ¬τ39) ∧
(¬⟦(= λ17 12)⟧ ∨ ¬τ39) ∧
(⟦(= λ15 11)⟧ ∨ ¬τ39 ∨ τ40) ∧
(⟦(= λ15 11)⟧ ∨ τ39 ∨ ¬τ40) ∧
(¬⟦(= λ15 11)⟧ ∨ ¬τ40) ∧
(⟦(= λ15 10)⟧ ∨ ¬τ40 ∨ τ41) ∧
(⟦(= λ15 10)⟧ ∨ τ40 ∨ ¬τ41) ∧
(¬⟦(= λ15 10)⟧ ∨ ¬τ41) ∧
(τ21 ∨ ¬τ41 ∨ τ42) ∧
(τ21 ∨ τ41 ∨ ¬τ42) ∧
(¬τ21 ∨ ¬τ42) ∧
(τ20 ∨ ¬τ42 ∨ τ43) ∧
(τ20 ∨ τ42 ∨ ¬τ43) ∧
(¬τ20 ∨ ¬τ43) ∧
(τ19 ∨ ¬τ43 ∨ τ44) ∧
(τ19 ∨ τ43 ∨ ¬τ44) ∧
(¬τ19 ∨ ¬τ44) ∧
(τ18 ∨ ¬τ44 ∨ τ45) ∧
(τ18 ∨ τ44 ∨ ¬τ45) ∧
(¬τ18 ∨ ¬τ45) ∧
(¬τ17 ∨ ¬τ45 ∨ τ46) ∧
(¬τ17 ∨ τ45 ∨ ¬τ46) ∧
(τ17 ∨ ¬τ46) ∧
(¬τ46 ∨ ¬⟦(= (ite (ite (ite (ite λ1113 false true) (ite (ite λ38 false λ1124) false true) false) false true) λ2073 (ite λ2076 λ2073 (ite (ite (ite λ38 λ1977 λ1982) false true) (ite (ite λ2076 false true) (ite (= λ2079 12) true (ite (= λ2079 14) true (ite (= λ2079 13) true (ite (= λ2079 15) (BRANCH_CONDITION (ite (= λ2094 0) 0 (ite (= λ2094 2) λ2105 (ite (= λ2094 1) λ2106 (ite (ite λ2107 λ2110 false) λ2111 (ite λ2107 λ2112 (ite (= λ2094 3) λ2113 (ite λ38 (select λ2117 λ2080) λ2068))))))) (ite (= λ2119 0) 0 (ite (= λ2119 2) λ2105 (ite (= λ2119 1) λ2106 (ite (ite λ2120 λ2110 false) λ2111 (ite λ2120 λ2112 (ite (= λ2119 3) λ2113 (ite λ38 (select λ2117 λ2118) λ2072)))))))) false)))) false) false))) (ite λ26 (ite λ26 (ite (= λ1074 10) λ1099 (ite (= λ1074 12) λ1100 (ite (= λ1074 14) λ1100 (ite (= λ1074 13) λ1100 (ite (= λ1074 15) (ite λ1082 (ite (BRANCH_CONDITION (ite (= λ1101 0) 0 (select λ1111 λ1101)) (ite (= λ1112 0) 0 (select λ1111 λ1112))) true λ1099) λ1099) λ1099))))) λ1099) λ1080))⟧ ∨ τ47) ∧
(¬τ46 ∨ ⟦(= (ite (ite (ite (ite λ1113 false true) (ite (ite λ38 false λ1124) false true) false) false true) λ2073 (ite λ2076 λ2073 (ite (ite (ite λ38 λ1977 λ1982) false true) (ite (ite λ2076 false true) (ite (= λ2079 12) true (ite (= λ2079 14) true (ite (= λ2079 13) true (ite (= λ2079 15) (BRANCH_CONDITION (ite (= λ2094 0) 0 (ite (= λ2094 2) λ2105 (ite (= λ2094 1) λ2106 (ite (ite λ2107 λ2110 false) λ2111 (ite λ2107 λ2112 (ite (= λ2094 3) λ2113 (ite λ38 (select λ2117 λ2080) λ2068))))))) (ite (= λ2119 0) 0 (ite (= λ2119 2) λ2105 (ite (= λ2119 1) λ2106 (ite (ite λ2120 λ2110 false) λ2111 (ite λ2120 λ2112 (ite (= λ2119 3) λ2113 (ite λ38 (select λ2117 λ2118) λ2072)))))))) false)))) false) false))) (ite λ26 (ite λ26 (ite (= λ1074 10) λ1099 (ite (= λ1074 12) λ1100 (ite (= λ1074 14) λ1100 (ite (= λ1074 13) λ1100 (ite (= λ1074 15) (ite λ1082 (ite (BRANCH_CONDITION (ite (= λ1101 0) 0 (select λ1111 λ1101)) (ite (= λ1112 0) 0 (select λ1111 λ1112))) true λ1099) λ1099) λ1099))))) λ1099) λ1080))⟧ ∨ ¬τ47) ∧
(τ46 ∨ τ47) ∧
(¬τ47)

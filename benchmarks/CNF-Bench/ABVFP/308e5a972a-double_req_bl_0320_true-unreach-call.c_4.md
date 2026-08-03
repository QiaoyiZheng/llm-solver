(⟦(= |c_cos_double_#t~ret139_primed| |c___kernel_cos_#res|)⟧) ∧
(¬τ1 ∨ ⟦(= |c_old(#memory_int)| |c_#memory_int_Hier|)⟧) ∧
(¬τ1 ∨ ⟦(= |c_old(#length)| |c_#length_Hier|)⟧) ∧
(¬τ1 ∨ ⟦(= |c_old(#valid)| |c_#valid_Hier|)⟧) ∧
(τ1 ∨ ¬⟦(= |c_old(#memory_int)| |c_#memory_int_Hier|)⟧ ∨ ¬⟦(= |c_old(#length)| |c_#length_Hier|)⟧ ∨ ¬⟦(= |c_old(#valid)| |c_#valid_Hier|)⟧) ∧
(τ1) ∧
(¬τ2 ∨ ⟦(= |c___kernel_cos_#in~x| c_cos_double_~x_Hier)⟧) ∧
(¬τ2 ∨ ⟦(= |c___kernel_cos_#in~y| c_cos_double_~z~4_Hier)⟧) ∧
(τ2 ∨ ¬⟦(= |c___kernel_cos_#in~x| c_cos_double_~x_Hier)⟧ ∨ ¬⟦(= |c___kernel_cos_#in~y| c_cos_double_~z~4_Hier)⟧) ∧
(τ2) ∧
(¬τ3 ∨ ⟦(= |c_cos_double_#in~x_Hier| c_cos_double_~x_Hier)⟧) ∧
(¬τ3 ∨ ⟦(exists ((v_skolemized_v_prenex_18_3 (_ BitVec 64))) (and (= |c_cos_double_#in~x_Hier| (fp ((_ extract 63 63) v_skolemized_v_prenex_18_3) ((_ extract 62 52) v_skolemized_v_prenex_18_3) ((_ extract 51 0) v_skolemized_v_prenex_18_3))) (= c_cos_double_~ix~3_Hier (bvand (_ bv2147483647 32) ((_ extract 63 32) v_skolemized_v_prenex_18_3)))))⟧) ∧
(τ3 ∨ ¬⟦(= |c_cos_double_#in~x_Hier| c_cos_double_~x_Hier)⟧ ∨ ¬⟦(exists ((v_skolemized_v_prenex_18_3 (_ BitVec 64))) (and (= |c_cos_double_#in~x_Hier| (fp ((_ extract 63 63) v_skolemized_v_prenex_18_3) ((_ extract 62 52) v_skolemized_v_prenex_18_3) ((_ extract 51 0) v_skolemized_v_prenex_18_3))) (= c_cos_double_~ix~3_Hier (bvand (_ bv2147483647 32) ((_ extract 63 32) v_skolemized_v_prenex_18_3)))))⟧) ∧
(τ3) ∧
(¬⟦(exists ((v_skolemized_v_prenex_18_3 (_ BitVec 64))) (and (bvsge (bvand (_ bv2147483647 32) ((_ extract 63 32) v_skolemized_v_prenex_18_3)) (_ bv2146435072 32)) (= |c_cos_double_#in~x_Hier| (fp ((_ extract 63 63) v_skolemized_v_prenex_18_3) ((_ extract 62 52) v_skolemized_v_prenex_18_3) ((_ extract 51 0) v_skolemized_v_prenex_18_3)))))⟧)
